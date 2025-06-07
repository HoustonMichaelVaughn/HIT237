import math
import csv

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from mango_pests.forms import PestSelectionForm, SampleSizeForm
from mango_pests.models import FarmBlock, PestCheck, Pest
from mango_pests.data import Pestsdiseases

from .forms import RegisterUserForm


class Login(DjangoLoginView):
    template_name = "growers/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)


class RegisterUser(FormView):
    template_name = "growers/register.html"
    success_url = reverse_lazy("profile")
    form_class = RegisterUserForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required
def profile_view(request):

    farm_blocks = FarmBlock.objects.filter(grower=request.user)
    raw_checks_qs = PestCheck.objects.filter(
        farm_block__grower=request.user
    ).order_by("-date_checked")

    # Compute confidence for each check
    all_checks = []
    for c in raw_checks_qs:

        n = getattr(c, "num_trees", 0)

        if getattr(c, "positives", 0) == 0 and n > 0:
            computed_conf = 100 * (1 - (1 - 0.01) ** n)

        else:
          computed_conf = 0.0
        setattr(c, "confidence", computed_conf)
        all_checks.append(c)

    # Filter by status
    status = request.GET.get("status", "all").lower()


    if status == "high":
        filtered_checks = [c for c in all_checks if c.confidence >= 90]
    elif status == "medium":
        filtered_checks = [c for c in all_checks if 50 <= c.confidence < 90]
    elif status == "low":
        filtered_checks = [c for c in all_checks if c.confidence < 50]

    else:

        filtered_checks = list(all_checks)

    # Totals
    total_blocks = farm_blocks.count()
    total_checks = len(all_checks)

    # Pagination helpers
    fb_search = request.GET.get("fb_search", "").strip().lower()
    farm_blocks_qs = farm_blocks.filter(name__icontains=fb_search) if fb_search else farm_blocks
    fb_paginator = Paginator(farm_blocks_qs, 5)
    farm_blocks_page = fb_paginator.get_page(request.GET.get("fb_page", 1))

    pc_search = request.GET.get("pc_search", "").strip().lower()
    pc_filtered = [
        c for c in filtered_checks
        if pc_search in c.pest.name.lower() or pc_search in c.farm_block.name.lower()
    ] if pc_search else filtered_checks
    pc_paginator = Paginator(pc_filtered, 5)
    recent_pest_checks_page = pc_paginator.get_page(request.GET.get("pc_page", 1))

    # Static + DB pests
    db_pests = list(Pest.objects.all())

    static_pests = [
        type("StaticPest", (), {
            "name": p.cardtitle,
            "scientific_name": getattr(p, "scientific_name", ""),
            "description": p.detailedinfo,
            "plant_type": type("PlantType", (), {"name": "Mango"})(),
            "is_static": True,
        })()
        for p in Pestsdiseases
    ]
    pests = db_pests + static_pests
    pest_search = request.GET.get("pest_search", "").strip().lower()
    if pest_search:
        pests = [
            p for p in pests
            if pest_search in p.name.lower()
            or (hasattr(p, "scientific_name") and pest_search in (p.scientific_name or "").lower())
        ]

    pest_type = request.GET.get("pest_type", "all").lower()
    if pest_type == "base":
        pests = [p for p in pests if getattr(p, "is_static", False)]
    elif pest_type == "user":
        pests = [p for p in pests if not getattr(p, "is_static", False)]

    pest_paginator = Paginator(pests, 5)
    pests_page = pest_paginator.get_page(request.GET.get("pest_page", 1))

    # Forms
    form = PestSelectionForm(request.POST or None, prefix="surv")
    sample_form = SampleSizeForm(request.POST or None, prefix="sample")

    surveillance_result = None
    sample_size_result = None

    # Surveillance confidence calculation
    if "surv-pest" in request.POST and form.is_valid():
        pest = form.cleaned_data["pest"]
        checks = PestCheck.objects.filter(pest=pest, positives=0, farm_block__grower=request.user)
        total_checked = sum(c.num_trees for c in checks)
        confidence = 100 * (1 - (1 - 0.01) ** total_checked) if total_checked > 0 else None
        surveillance_result = {"pest": pest, "total_checked": total_checked, "confidence": confidence}

    # Sample-size calculation
    if "sample-prevalence" in request.POST and sample_form.is_valid():
        p = sample_form.cleaned_data["prevalence"]
        c_val = sample_form.cleaned_data["confidence"]
        required_n = math.ceil(math.log(1 - c_val) / math.log(1 - p)) if p > 0 and c_val > 0 else None
        sample_size_result = {"prevalence": p, "confidence": c_val, "required_n": required_n}

    return render(request, "growers/profile.html", {
        "farm_blocks": farm_blocks_page,
        "recent_pest_checks": recent_pest_checks_page,
        "status_filter": status,
        "total_blocks": total_blocks,
        "total_checks": total_checks,
        "form": form,
        "surveillance_result": surveillance_result,
        "sample_form": sample_form,
        "sample_size_result": sample_size_result,
        "pests": pests_page,
        "fb_search": fb_search,
        "pc_search": pc_search,
        "pest_search": pest_search,
        "fb_paginator": fb_paginator,
        "pc_paginator": pc_paginator,
        "pest_paginator": pest_paginator,
    })

@login_required
def export_checks_csv(request):
    raw_checks = PestCheck.objects.filter(farm_block__grower=request.user).order_by("-date_checked")
    checks = []
    for c in raw_checks:
        n = getattr(c, "num_trees", 0)
        if getattr(c, "positives", 0) == 0 and n > 0:
            conf = 100 * (1 - (1 - 0.01) ** n)
        else:
            conf = 0.0
        setattr(c, "confidence", round(conf, 2))
        checks.append(c)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="pest_checks.csv"'
    writer = csv.writer(response)
    writer.writerow(["Date Checked", "Pest", "Farm Block", "Num Trees", "Positives", "Confidence (%)"])
    for c in checks:
        writer.writerow([
            c.date_checked,
            c.pest.name,
            c.farm_block.name,
            c.num_trees,
            c.positives,
            f"{c.confidence:.2f}"
        ])
    return response


@login_required
def ajax_farm_block_list(request):
    farm_blocks = FarmBlock.objects.filter(grower=request.user)
    fb_search = request.GET.get("fb_search", "").strip().lower()
    if fb_search:
        farm_blocks = farm_blocks.filter(name__icontains=fb_search)
    paginator = Paginator(farm_blocks, 5)
    page = paginator.get_page(request.GET.get("fb_page", 1))
    html = render_to_string("growers/partials/farm_blocks_table.html", {
        "farm_blocks": page, "fb_search": fb_search
    }, request=request)
    return HttpResponse(html)


@login_required
def ajax_pest_check_list(request):
    raw_checks = PestCheck.objects.filter(farm_block__grower=request.user).order_by("-date_checked")
    all_checks = []
    for c in raw_checks:
        n = getattr(c, "num_trees", 0)
        conf = 100 * (1 - (1 - 0.01) ** n) if getattr(c, "positives", 0) == 0 and n > 0 else 0.0
        c.confidence = conf
        all_checks.append(c)

    pc_search = request.GET.get("pc_search", "").strip().lower()
    filtered = [
        c for c in all_checks
        if pc_search in c.pest.name.lower() or pc_search in c.farm_block.name.lower()
    ] if pc_search else all_checks

    paginator = Paginator(filtered, 5)
    page = paginator.get_page(request.GET.get("pc_page", 1))
    html = render_to_string("growers/partials/pest_checks_table.html", {
        "recent_pest_checks": page, "pc_search": pc_search
    }, request=request)
    return HttpResponse(html)


@login_required
def ajax_pest_list(request):

    db_pests = list(Pest.objects.all())
    static_pests = [
        type("StaticPest", (), {
            "name": p.cardtitle,
            "scientific_name": getattr(p, "scientific_name", ""),
            "description": p.detailedinfo,
            "plant_type": type("PlantType", (), {"name": "Mango"})(),
            "is_static": True,
        })()
        for p in Pestsdiseases
    ]
    pests = db_pests + static_pests

    pest_search = request.GET.get("pest_search", "").strip().lower()

    if pest_search:
        pests = [
            p for p in pests
            if pest_search in p.name.lower()
            or (hasattr(p, "scientific_name") and pest_search in (p.scientific_name or "").lower())
        ]

    pest_type = request.GET.get("pest_type", "all").lower()
    if pest_type == "base":
        pests = [p for p in pests if getattr(p, "is_static", False)]
    elif pest_type == "user":
        pests = [p for p in pests if not getattr(p, "is_static", False)]

    paginator = Paginator(pests, 5)
    page = paginator.get_page(request.GET.get("pest_page", 1))
    html = render_to_string("growers/partials/pests_table.html", {
        "pests": page, "pest_search": pest_search
    }, request=request)
    return HttpResponse(html)