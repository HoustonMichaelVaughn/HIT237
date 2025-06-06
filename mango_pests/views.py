from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpRequest
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from mango_pests.forms import PestSelectionForm, SampleSizeForm
import math
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import HttpResponse
from .data import Pestsdiseases, References
from mango_pests.data import Pestsdiseases
from mango_pests.models import Pest
from .forms import PestForm, FarmBlockForm, PestCheckForm
from .models import FarmBlock, PestCheck


# Static Views
def home(request):
    return render(request, "mango_pests/home.html")

class PestListView(View):
    def get(self, request):
        search = request.GET.get("search", "").lower()

        pestcards = [
            pest.__dict__ for pest in Pestsdiseases
            if search in pest.cardtitle.lower()
        ] if search else [pest.__dict__ for pest in Pestsdiseases]

        user_pests = Pest.objects.filter(owner=request.user) if request.user.is_authenticated else []
        for p in user_pests:
            pestcards.append({
                "cardtitle": p.name,
                "cardsubtitle": p.scientific_name,
                "cardtext": p.description[:150] + "...",
                "img": p.image.url if p.image else "default.jpg",
                "link": "#",  # Update if you have pest detail pages
            })

        return render(request, "mango_pests/project_list.html", {
            "pestcards": pestcards,
            "search": search,
        })

class PestDetailView(View):
    def get(self, request, slugurl):
        pestdetails = next((pest.__dict__ for pest in Pestsdiseases if pest.urlslug == slugurl), None)
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

# CRUD Views (shared template logic)

@login_required
def create_pest(request):
    form = PestForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("pestlist")
    return render(request, "mango_pests/farm_check_add.html", {"form": form, "title": "Add Pest", "button_label": "Create"})


@login_required
def edit_pest(request, pk):
    pest = get_object_or_404(Pest, pk=pk, owner=request.user)
    if request.method == "POST":
        form = PestForm(request.POST, request.FILES, instance=pest)
        if form.is_valid():
            form.save()
            return redirect("pestlist")
    else:
        form = PestForm(instance=pest)
    return render(request, "mango_pests/farm_check_add.html", {"form": form, "edit": True})

@login_required
def delete_pest(request, pk):
    pest = get_object_or_404(Pest, pk=pk, owner=request.user)
    if request.method == "POST":
        pest.delete()
        return redirect("pestlist")
    return render(request, "mango_pests/pest_confirm_delete.html", {"pest": pest})

@login_required
def add_farm_block(request):
    form = FarmBlockForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        farm_block = form.save(commit=False)
        farm_block.grower = request.user
        farm_block.save()
        return redirect("profile")
    return render(request, "mango_pests/farm_check_add.html", {"form": form, "title": "Add Farm Block", "button_label": "Create"})

@login_required
def create_pest_check(request):
    form = PestCheckForm(request.POST or None, user=request.user)
    if request.method == "POST" and form.is_valid():
        pest_check = form.save()
        return redirect("profile")
    return render(request, "mango_pests/farm_check_add.html", {"form": form, "title": "Log New Pest Check", "button_label": "Create"})

# Update Views
class FarmBlockUpdateView(LoginRequiredMixin, UpdateView):
    model = FarmBlock
    form_class = FarmBlockForm
    template_name = "mango_pests/farm_check_add.html"

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Edit Farm Block \"{self.object.name}\""
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

# Delete Views
class FarmBlockDeleteView(LoginRequiredMixin, DeleteView):
    model = FarmBlock
    template_name = "mango_pests/farm_check_remove.html"
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confirm_message"] = f"Are you sure you want to delete the farm block \"{self.object.name}\"?"
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

def ajax_confidence_result(request):
    form = PestSelectionForm(request.POST or None, prefix='surv')
    result_html = ""

    if form.is_valid():
        pest = form.cleaned_data['pest']
        checks = PestCheck.objects.filter(
            pest=pest,
            positives=0,
            farm_block__grower=request.user
        )
        total_checked = sum(c.num_trees for c in checks)
        if total_checked > 0:
            confidence = 100 * (1 - (1 - 0.01) ** total_checked)
        else:
            confidence = None

        result_html = render_to_string("mango_pests/partials/confidence_result.html", {
            "surveillance_result": {
                "pest": pest,
                "total_checked": total_checked,
                "confidence": confidence,
            }
        })

    return HttpResponse(result_html)

def ajax_sample_result(request):
    form = SampleSizeForm(request.POST or None, prefix='sample')
    result_html = ""

    if form.is_valid():
        p = form.cleaned_data['prevalence']
        c_val = form.cleaned_data['confidence']

        if p > 0 and c_val > 0:
            required_n = math.ceil(math.log(1 - c_val) / math.log(1 - p))
        else:
            required_n = None

        result_html = render_to_string("mango_pests/partials/sample_size_result.html", {
            "sample_size_result": {
                "prevalence": p,
                "confidence": c_val,
                "required_n": required_n,
            }
        })

    return HttpResponse(result_html)