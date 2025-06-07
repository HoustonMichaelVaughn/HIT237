import math

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from mango_pests.forms import PestSelectionForm, SampleSizeForm
from mango_pests.models import FarmBlock, PestCheck
from mango_pests.data import Pestsdiseases  # <-- import static pests

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
    # A)Fetch all FarmBlock and PestCheck objects for this user,
    #    then compute a “confidence” value (0–100) on each PestCheck in Python.
    farm_blocks = FarmBlock.objects.filter(grower=request.user)
    raw_checks_qs = PestCheck.objects.filter(farm_block__grower=request.user).order_by(
        "-date_checked"
    )

    # A1) Build a new list `all_checks` so that each PestCheck has `.confidence` attached
    all_checks = []
    for c in raw_checks_qs:
        n = getattr(c, "num_trees", 0)
        # If there were zero positives, compute binomial confidence at 1% prevalence
        if getattr(c, "positives", 0) == 0 and n > 0:
            computed_conf = 100 * (1 - (1 - 0.01) ** n)
        else:
            # If positives > 0 (or n == 0), treat confidence as 0
            computed_conf = 0.0

        # Attach attribute to this instance for later use
        setattr(c, "confidence", computed_conf)
        all_checks.append(c)

    # B) Read the “status” GET parameter (default = "all")
    status = request.GET.get("status", "all").lower()

    # C) Manually filter the Python list by the computed `.confidence` property
    if status == "high":
        # Keep only those checks whose confidence ≥ 90
        filtered_checks = [c for c in all_checks if getattr(c, "confidence", 0) >= 90]
    elif status == "medium":
        # Keep only those checks with 50 ≤ confidence < 90
        filtered_checks = [
            c for c in all_checks if 50 <= getattr(c, "confidence", 0) < 90
        ]
    elif status == "low":
        # Keep only those checks with confidence < 50
        filtered_checks = [c for c in all_checks if getattr(c, "confidence", 0) < 50]
    else:
        # “all” or any other value → show all checks in this case
        filtered_checks = list(all_checks)

    # D) Totals for summary cards
    total_blocks = farm_blocks.count()
    total_checks = len(all_checks)  # count of all checks (unfiltered)

    # E) Only show the first 5 in the Recent Pest Checks table
    recent_pest_checks = filtered_checks[:5]

    # Fetch all pests for display in dashboard (DB + static)
    from mango_pests.models import Pest

    db_pests = list(Pest.objects.all())
    # Wrap static pests as dicts with DB-like fields for template compatibility
    static_pests = [
        type('StaticPest', (), {
            'name': p.cardtitle,
            'scientific_name': getattr(p, 'scientific_name', ''),
            'description': p.detailedinfo,
            'plant_type': type('PlantType', (), {'name': 'Mango'})(),
            'is_static': True
        })() for p in Pestsdiseases
    ]
    pests = db_pests + static_pests

    # F) Two separate forms with prefixes (for the calculators)
    form = PestSelectionForm(request.POST or None, prefix="surv")
    sample_form = SampleSizeForm(request.POST or None, prefix="sample")

    surveillance_result = None
    sample_size_result = None

    # G) If “Check My Surveillance Confidence” form was submitted:
    if "surv-pest" in request.POST and form.is_valid():
        pest = form.cleaned_data["pest"]
        checks = PestCheck.objects.filter(
            pest=pest, positives=0, farm_block__grower=request.user
        )
        total_checked = sum(c.num_trees for c in checks)
        if total_checked > 0:
            # 1% prevalence → probability of ≥1 detection
            confidence = 100 * (1 - (1 - 0.01) ** total_checked)
        else:
            confidence = None
        surveillance_result = {
            "pest": pest,
            "total_checked": total_checked,
            "confidence": confidence,
        }

    # H) If “How Many Trees Should I Check?” form was submitted:
    if "sample-prevalence" in request.POST and sample_form.is_valid():
        p = sample_form.cleaned_data["prevalence"]  # e.g. 0.01
        c_val = sample_form.cleaned_data["confidence"]  # e.g. 0.95
        if p > 0 and c_val > 0:
            required_n = math.ceil(math.log(1 - c_val) / math.log(1 - p))
        else:
            required_n = None
        sample_size_result = {
            "prevalence": p,
            "confidence": c_val,
            "required_n": required_n,
        }

    # Search and pagination for Farm Blocks
    fb_search = request.GET.get("fb_search", "").strip().lower()
    farm_blocks_qs = farm_blocks
    if fb_search:
        farm_blocks_qs = farm_blocks_qs.filter(name__icontains=fb_search)
    fb_page = request.GET.get("fb_page", 1)
    fb_paginator = Paginator(farm_blocks_qs, 5)
    farm_blocks_page = fb_paginator.get_page(fb_page)

    # Search and pagination for Pest Checks
    pc_search = request.GET.get("pc_search", "").strip().lower()
    filtered_checks_qs = filtered_checks
    if pc_search:
        filtered_checks_qs = [c for c in filtered_checks if pc_search in c.pest.name.lower() or pc_search in c.farm_block.name.lower()]
    pc_page = request.GET.get("pc_page", 1)
    pc_paginator = Paginator(filtered_checks_qs, 5)
    recent_pest_checks_page = pc_paginator.get_page(pc_page)

    # Search and pagination for Pests
    pest_search = request.GET.get("pest_search", "").strip().lower()
    pest_type = request.GET.get("pest_type", "all").lower()  # new filter
    pests_qs = pests
    if pest_search:
        pests_qs = [p for p in pests if pest_search in p.name.lower() or (hasattr(p, 'scientific_name') and pest_search in (p.scientific_name or '').lower())]
    # Filter by pest_type
    if pest_type == "base":
        pests_qs = [p for p in pests_qs if getattr(p, 'is_static', False)]
    elif pest_type == "user":
        pests_qs = [p for p in pests_qs if not getattr(p, 'is_static', False)]
    pest_page = request.GET.get("pest_page", 1)
    pest_paginator = Paginator(pests_qs, 5)
    pests_page = pest_paginator.get_page(pest_page)

    # I) Render the template with all context
    return render(
        request,
        "growers/profile.html",
        {
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
        },
    )


@login_required
def ajax_farm_block_list(request):
    farm_blocks = FarmBlock.objects.filter(grower=request.user)
    fb_search = request.GET.get("fb_search", "").strip().lower()
    if fb_search:
        farm_blocks = farm_blocks.filter(name__icontains=fb_search)
    fb_page = request.GET.get("fb_page", 1)
    fb_paginator = Paginator(farm_blocks, 5)
    farm_blocks_page = fb_paginator.get_page(fb_page)
    html = render_to_string(
        "growers/partials/farm_blocks_table.html",
        {"farm_blocks": farm_blocks_page, "fb_search": fb_search},
        request=request,
    )
    return HttpResponse(html)


@login_required
def ajax_pest_check_list(request):
    # Rebuild the same logic as in profile_view for pest checks
    from mango_pests.models import PestCheck
    raw_checks_qs = PestCheck.objects.filter(farm_block__grower=request.user).order_by("-date_checked")
    all_checks = []
    for c in raw_checks_qs:
        n = getattr(c, "num_trees", 0)
        if getattr(c, "positives", 0) == 0 and n > 0:
            computed_conf = 100 * (1 - (1 - 0.01) ** n)
        else:
            computed_conf = 0.0
        c.confidence = computed_conf
        all_checks.append(c)
    # Filtering
    pc_search = request.GET.get("pc_search", "").strip().lower()
    filtered_checks = all_checks
    if pc_search:
        filtered_checks = [c for c in all_checks if pc_search in c.pest.name.lower() or pc_search in c.farm_block.name.lower()]
    pc_page = request.GET.get("pc_page", 1)
    pc_paginator = Paginator(filtered_checks, 5)
    recent_pest_checks_page = pc_paginator.get_page(pc_page)
    html = render_to_string(
        "growers/partials/pest_checks_table.html",
        {"recent_pest_checks": recent_pest_checks_page, "pc_search": pc_search},
        request=request,
    )
    return HttpResponse(html)


@login_required
def ajax_pest_list(request):
    from mango_pests.models import Pest
    from mango_pests.data import Pestsdiseases
    # Build DB and static pest list as in profile_view
    db_pests = list(Pest.objects.all())
    static_pests = [
        type('StaticPest', (), {
            'name': p.cardtitle,
            'scientific_name': getattr(p, 'scientific_name', ''),
            'description': p.detailedinfo,
            'plant_type': type('PlantType', (), {'name': 'Mango'})(),
            'is_static': True
        })() for p in Pestsdiseases
    ]
    pests = db_pests + static_pests
    pest_search = request.GET.get("pest_search", "").strip().lower()
    pest_type = request.GET.get("pest_type", "all").lower()  # new filter
    if pest_search:
        pests = [p for p in pests if pest_search in p.name.lower() or (hasattr(p, 'scientific_name') and pest_search in (p.scientific_name or '').lower())]
    # Filter by pest_type
    if pest_type == "base":
        pests = [p for p in pests if getattr(p, 'is_static', False)]
    elif pest_type == "user":
        pests = [p for p in pests if not getattr(p, 'is_static', False)]
    pest_page = request.GET.get("pest_page", 1)
    from django.core.paginator import Paginator
    pest_paginator = Paginator(pests, 5)
    pests_page = pest_paginator.get_page(pest_page)
    html = render_to_string(
        "growers/partials/pests_table.html",
        {"pests": pests_page, "pest_search": pest_search},
        request=request,
    )
    return HttpResponse(html)