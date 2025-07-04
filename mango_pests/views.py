import math

from django.contrib import messages  # Used for displaying one-time messages to users.
from django.contrib.auth.decorators import login_required  # Decorator to restrict access to logged-in users.
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin to restrict class-based views to logged-in users.
from django.core.paginator import Paginator  # Utility for paginating querysets.
from django.http import Http404, HttpRequest, HttpResponse  # HTTP utilities for handling requests and responses.
from django.shortcuts import redirect, render, get_object_or_404  # Shortcuts for common view operations.
from django.template.loader import render_to_string  # Utility for rendering templates to strings.
from django.urls import reverse_lazy  # Utility for lazy URL resolution.
from django.views import View  # Base class for all views.
from django.views.generic.edit import DeleteView, UpdateView  # Generic views for editing models.

from mango_pests.forms import PestSelectionForm, SampleSizeForm

from .data import Pestsdiseases, References
from .forms import FarmBlockForm, PestCheckForm, PestForm
from .models import FarmBlock, Pest, PestCheck, PlantType


# Static Views
def home(request):
    return render(request, "mango_pests/home.html")


# Added a fallback image for pests without an image.
# Define a fallback image URL
FALLBACK_IMAGE_URL = "/static/images/default_fallback_image.png"


class PestListView(View):
    def get(self, request: HttpRequest):
        search = request.GET.get("search", "").lower()
        page_number = request.GET.get("page", 1)

        # Static pests
        static_pests = (
            [
                pest.__dict__
                for pest in Pestsdiseases
                if search in pest.cardtitle.lower()
            ]
            if search
            else [pest.__dict__ for pest in Pestsdiseases]
        )

        # Database pests
        db_pests_qs = Pest.objects.all()
        if search:
            db_pests_qs = db_pests_qs.filter(name__icontains=search)
        db_pests = []
        for pest in db_pests_qs:
            db_pests.append(
                {
                    "cardtitle": pest.name,
                    "cardtext": pest.description[:120]
                    + ("..." if len(pest.description) > 120 else ""),
                    "urlslug": pest.name.lower().replace(" ", "-"),
                    "image": pest.image.url if pest.image else FALLBACK_IMAGE_URL,
                    "is_db": True,
                    "id": pest.id,
                }
            )

        # Combine and paginate
        all_pests = static_pests + db_pests
        paginator = Paginator(all_pests, 7)
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "mango_pests/project_list.html",
            {
                "pestcards": page_obj.object_list,
                "search": search,
                "page_obj": page_obj,
            },
        )


class PestDetailView(View):
    def get(self, request, slugurl):
        pestdetails = next(
            (pest.__dict__ for pest in Pestsdiseases if pest.urlslug == slugurl), None
        )
        return render(request, "mango_pests/project_detail.html", {"pestdetails": pestdetails})


class AboutView(View):
    def get(self, request):
        aboutcards = [
            {"membername": "Houston Vaughn", "aboutmember": "A computer science student at CDU. Teamleader for Group 7"},
            {"membername": "Neolisa De Castro", "aboutmember": "Computer Science Student."},
            {"membername": "Gislene Freitas De Lima Clancy", "aboutmember": "A computer science student at CDU."},
            {"membername": "Dean Metcalfe", "aboutmember": "A computer science student at CDU."},
        ]
        return render(request, "mango_pests/about.html", {"aboutcards": aboutcards})


class ReferencesView(View):
    def get(self, request):
        return render(request, "mango_pests/references.html", {"references": References})


# CRUD Views
@login_required
def create_pest(request):
    form = PestForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile")
    return render(
        request,
        "mango_pests/farm_check_add.html",
        {"form": form, "title": "Add Pest", "button_label": "Create"},
    )


@login_required
def add_farm_block(request):
    form = FarmBlockForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        farm_block = form.save(commit=False)
        farm_block.grower = request.user
        farm_block.save()
        return redirect("profile")
    return render(
        request,
        "mango_pests/farm_check_add.html",
        {"form": form, "title": "Add Farm Block", "button_label": "Create"},
    )


@login_required
def create_pest_check(request):
    form = PestCheckForm(request.POST or None, user=request.user)

    if request.method == "POST" and form.is_valid():
        real_pest = form.cleaned_data.get("real_pest")
        static_pest = form.cleaned_data.get("static_pest")

        if real_pest and static_pest:
            messages.error(request, "Please select only one pest source: database or static.")
            return redirect("pestcheck:new")

        if not real_pest and not static_pest:
            messages.error(request, "You must select a pest.")
            return redirect("pestcheck:new")

        if static_pest:
            # Handle static pest lookup and conversion
            try:
                idx = int(static_pest.split("::")[1])
                static_def = Pestsdiseases[idx]
            except (IndexError, ValueError):
                messages.error(request, "Invalid static pest selected.")
                return redirect("pestcheck:new")

            # Check if a matching Pest already exists
            pest_obj, _ = Pest.objects.get_or_create(
                name=static_def.cardtitle,
                defaults={
                    "description": static_def.detailedinfo,
                    "scientific_name": getattr(static_def, "scientific_name", ""),
                    "plant_type": PlantType.objects.first(),  # Or choose smarter default
                    "owner": request.user,
                },
            )

            # Mutate POST data to use the resolved pest ID
            post = request.POST.copy()
            post["real_pest"] = str(pest_obj.pk)
            post["static_pest"] = ""
            form = PestCheckForm(post, request.FILES or None, user=request.user)

        if form.is_valid():
            pest_check = form.save(commit=False)
            if static_pest:
                pest_check.pest = pest_obj
            else:
                pest_check.pest = real_pest
            pest_check.save()
            form.save_m2m()
            messages.success(request, "Pest check logged successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Failed to log pest check.")

    return render(
        request,
        "mango_pests/farm_check_add.html",
        {"form": form, "title": "Log New Pest Check", "button_label": "Create"},
    )



# Update Views
class FarmBlockUpdateView(LoginRequiredMixin, UpdateView):
    model = FarmBlock
    form_class = FarmBlockForm
    template_name = "mango_pests/farm_check_add.html"

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Edit Farm Block "{self.object.name}"'
        context["button_label"] = "Save Changes"
        return context

    def get_success_url(self):
        return reverse_lazy("profile")


class PestCheckUpdateView(LoginRequiredMixin, UpdateView):
    model = PestCheck
    form_class = PestCheckForm
    template_name = "mango_pests/farm_check_add.html"
    success_url = reverse_lazy("profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.farm_block.grower != self.request.user:
            raise Http404("You do not have permission to edit this pest check.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Pest Check"
        context["button_label"] = "Save Changes"
        return context


class PestUpdateView(LoginRequiredMixin, UpdateView):
    model = Pest
    form_class = PestForm
    template_name = "mango_pests/farm_check_add.html"
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Edit Pest '{self.object.name}'"
        context["button_label"] = "Save Changes"
        return context


# Delete Views
class FarmBlockDeleteView(LoginRequiredMixin, DeleteView):
    model = FarmBlock
    template_name = "mango_pests/farm_check_remove.html"
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confirm_message"] = f'Are you sure you want to delete the farm block "{self.object.name}"?'
        return context


class PestCheckDeleteView(LoginRequiredMixin, DeleteView):
    model = PestCheck
    template_name = "mango_pests/farm_check_remove.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.farm_block.grower != self.request.user:
            raise Http404("You do not have permission to delete this pest check.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confirm_message"] = "Are you sure you want to delete this pest check?"
        return context


class PestDeleteView(LoginRequiredMixin, DeleteView):
    model = Pest
    template_name = "mango_pests/farm_check_remove.html"
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confirm_message"] = f"Are you sure you want to delete the pest '{self.object.name}'?"
        return context


# AJAX Views
def ajax_confidence_result(request):
    form = PestSelectionForm(request.POST or None, prefix="surv")
    result_html = ""

    if form.is_valid():
        pest = form.cleaned_data["pest"]
        checks = PestCheck.objects.filter(
            pest=pest, positives=0, farm_block__grower=request.user
        )
        total_checked = sum(c.num_trees for c in checks)
        if total_checked > 0:
            confidence = 100 * (1 - (1 - 0.01) ** total_checked)
        else:
            confidence = None

        result_html = render_to_string(
            "mango_pests/partials/confidence_result.html",
            {
                "surveillance_result": {
                    "pest": pest,
                    "total_checked": total_checked,
                    "confidence": confidence,
                }
            },
        )

    return HttpResponse(result_html)


def ajax_sample_result(request):
    form = SampleSizeForm(request.POST or None, prefix="sample")
    result_html = ""

    if form.is_valid():
        p = form.cleaned_data["prevalence"]
        c_val = form.cleaned_data["confidence"]

        if p > 0 and c_val > 0:
            required_n = math.ceil(math.log(1 - c_val) / math.log(1 - p))
        else:
            required_n = None

        result_html = render_to_string(
            "mango_pests/partials/sample_size_result.html",
            {
                "sample_size_result": {
                    "prevalence": p,
                    "confidence": c_val,
                    "required_n": required_n,
                }
            },
        )

    return HttpResponse(result_html)
