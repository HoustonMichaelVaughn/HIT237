from django.shortcuts import render
from django.http import HttpRequest
from .data import Pestsdiseases, References
from django.views import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PestForm
from .forms import FarmBlockForm
from django.http import Http404
from .forms import PestCheckForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import FarmBlock, PestCheck
from django.urls import reverse_lazy




# Sources
# https://docs.djangoproject.com/en/5.2/ref/request-response/
# https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint


def home(request):
    return render(request, "mango_pests/home.html")

def detection_confidence_report(request):
    # Get relevant pest checks (only where no positives were found)
    checks = PestCheck.objects.filter(num_positive=0)

    if not checks.exists():
        return render(request, "mango_pests/detection_report.html", {"data": None})

    # Prepare data for pandas
    data = [{
        "pest_name": check.pest.name,
        "farm_block": check.farm_block.name,
        "date": check.date_checked,
        "trees_checked": check.num_trees_checked
    } for check in checks]

    df = pd.DataFrame(data)

    # Calculate detection confidence assuming 1% prevalence
    assumed_prevalence = 0.01
    df['confidence_95'] = (1 - (1 - assumed_prevalence) ** df['trees_checked']).round(4)

    # Convert to records for template
    records = df.to_dict(orient='records')

    return render(request, "mango_pests/detection_report.html", {"data": records})

class FarmBlockUpdateView(LoginRequiredMixin, UpdateView):
    model = FarmBlock
    form_class = FarmBlockForm
    template_name = "mango_pests/farm_block_form.html"

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile")

class FarmBlockDeleteView(LoginRequiredMixin, DeleteView):
    model = FarmBlock
    template_name = "mango_pests/farm_block_confirm_delete.html"
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        return FarmBlock.objects.filter(grower=self.request.user)


class PestListView(View):
    #   Below is a type hint to get vs to recognise request as a HttpRequest! How cool is that?
    def get(self, request: HttpRequest):
        search = ""
        try:
            search = request.GET["search"].lower()
        except:
            pass
        if search:
            pestcards = [
                pest.__dict__
                for pest in Pestsdiseases
                if search in pest.cardtitle.lower()
            ]
        else:
            pestcards = [pest.__dict__ for pest in Pestsdiseases]
        return render(
            request,
            "mango_pests/project_list.html",
            {"pestcards": pestcards, "search": search},
        )


class PestDetailView(View):
    def get(self, request, slugurl):
        for pest in Pestsdiseases:
            if pest.urlslug == slugurl:
                pestdetails = pest.__dict__
                break
        return render(
            request, "mango_pests/project_detail.html", {"pestdetails": pestdetails}
        )


class AboutView(View):
    def get(self, request):
        aboutcards = [
            {
                "membername": "Houston Vaughn",
                "aboutmember": "A computer science student at CDU. Teamleader for Group 7",
            },
            {
                "membername": "Neolisa De Castro",
                "aboutmember": "Computer Science Student.",
            },
            {
                "membername": "Gislene Freitas De Lima Clancy",
                "aboutmember": "A computer science student at CDU.",
            },
            {
                "membername": "Dean Metcalfe",
                "aboutmember": "A computer science student at CDU.",
            },
        ]
        return render(request, "mango_pests/about.html", {"aboutcards": aboutcards})


class ReferencesView(View):
    def get(self, request):
        return render(
            request, "mango_pests/references.html", {"references": References}
        )
    
# Each user can have their own pests
@login_required
def create_pest(request):
    if request.method == "POST":
        form = PestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pestlist") 
    else:
        form = PestForm()
    return render(request, "mango_pests/pest_form.html", {"form": form})

@login_required
def add_farm_block(request):
    if request.method == "POST":
        form = FarmBlockForm(request.POST)
        if form.is_valid():
            farm_block = form.save(commit=False)
            farm_block.grower = request.user
            farm_block.save()
            return redirect("profile")
    else:
        form = FarmBlockForm()
    return render(request, "mango_pests/farm_block_form.html", {"form": form})

class PestCheckUpdateView(LoginRequiredMixin, UpdateView):
    model = PestCheck
    form_class = PestCheckForm
    template_name = "mango_pests/pest_check_form.html"
    success_url = "/growers/profile/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass user for farm block filtering
        return kwargs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.farm_block.grower != self.request.user:
            raise Http404("You do not have permission to edit this pest check.")
        return obj
    

class PestCheckDeleteView(LoginRequiredMixin, DeleteView):
    model = PestCheck
    template_name = "mango_pests/pest_check_confirm_delete.html"
    success_url = "/growers/profile/"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.farm_block.grower != self.request.user:
            raise Http404("You do not have permission to delete this pest check.")
        return obj


@login_required
def create_pest_check(request):
    if request.method == "POST":
        form = PestCheckForm(request.POST, user=request.user)
        if form.is_valid():
            pest_check = form.save(commit=False)
            pest_check.save()
            return redirect("profile")
    else:
        form = PestCheckForm(user=request.user)
    return render(request, "mango_pests/pest_check_form.html", {"form": form})