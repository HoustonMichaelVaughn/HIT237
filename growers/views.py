from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from mango_pests.models import FarmBlock, PestCheck
from .forms import RegisterUserForm
from mango_pests.forms import PestSelectionForm, SampleSizeForm 

import math
import csv
from django.http import HttpResponse

@login_required
def export_csv(request):
    """
    Export all PestCheck rows for the logged-in grower as a CSV.
    """
    #This is to  create the HTTP response with a CSV MIME type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pest_checks.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Pest',
        'Date Checked',
        'Block',
        'Trees Checked',
        'Positives',
        'Confidence (%)'
    ])

    # and this  filter the PestCheck objects by the grower (user)
    checks = PestCheck.objects.filter(farm_block__grower=request.user)
    for check in checks:
        writer.writerow([
            check.pest.name,
            check.date_checked,
            check.farm_block.name,
            check.num_trees,
            check.positives,
            check.confidence_score or 0,
        ])

    return response

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
    raw_checks_qs = PestCheck.objects.filter(
        farm_block__grower=request.user
    ).order_by('-date_checked')

    # A1) Build a new list `all_checks` so that each PestCheck has `.confidence` attached
    all_checks = []
    for c in raw_checks_qs:
        n = getattr(c, 'num_trees', 0)
        # If there were zero positives, compute binomial confidence at 1% prevalence
        if getattr(c, 'positives', 0) == 0 and n > 0:
            computed_conf = 100 * (1 - (1 - 0.01) ** n)
        else:
            # If positives > 0 (or n == 0), treat confidence as 0
            computed_conf = 0.0

        # Attach attribute to this instance for later use
        setattr(c, 'confidence', computed_conf)
        all_checks.append(c)

    # B) Read the “status” GET parameter (default = "all")
    status = request.GET.get("status", "all").lower()

    # C) Manually filter the Python list by the computed `.confidence` property
    if status == "high":
        # Keep only those checks whose confidence ≥ 90
        filtered_checks = [
            c for c in all_checks
            if getattr(c, 'confidence', 0) >= 90
        ]
    elif status == "medium":
        # Keep only those checks with 50 ≤ confidence < 90
        filtered_checks = [
            c for c in all_checks
            if 50 <= getattr(c, 'confidence', 0) < 90
        ]
    elif status == "low":
        # Keep only those checks with confidence < 50
        filtered_checks = [
            c for c in all_checks
            if getattr(c, 'confidence', 0) < 50
        ]
    else:
        # “all” or any other value → show all checks in this case 
        filtered_checks = list(all_checks)

    # D) Totals for summary cards
    total_blocks = farm_blocks.count()
    total_checks = len(all_checks)  # count of all checks (unfiltered)

    # E) Only show the first 5 in the Recent Pest Checks table
    recent_pest_checks = filtered_checks[:5]

    # F) Two separate forms with prefixes (for the calculators)
    form        = PestSelectionForm(request.POST or None, prefix='surv')
    sample_form = SampleSizeForm(request.POST or None, prefix='sample')

    surveillance_result = None
    sample_size_result  = None

    # G) If “Check My Surveillance Confidence” form was submitted:
    if 'surv-pest' in request.POST and form.is_valid():
        pest = form.cleaned_data['pest']
        checks = PestCheck.objects.filter(
            pest=pest,
            positives=0,
            farm_block__grower=request.user
        )
        total_checked = sum(c.num_trees for c in checks)
        if total_checked > 0:
            # 1% prevalence → probability of ≥1 detection
            confidence = 100 * (1 - (1 - 0.01) ** total_checked)
        else:
            confidence = None
        surveillance_result = {
            'pest': pest,
            'total_checked': total_checked,
            'confidence': confidence,
        }

    # H) If “How Many Trees Should I Check?” form was submitted:
    if 'sample-prevalence' in request.POST and sample_form.is_valid():
        p = sample_form.cleaned_data['prevalence']   # e.g. 0.01
        c_val = sample_form.cleaned_data['confidence']  # e.g. 0.95
        if p > 0 and c_val > 0:
            required_n = math.ceil(math.log(1 - c_val) / math.log(1 - p))
        else:
            required_n = None
        sample_size_result = {
            'prevalence': p,
            'confidence': c_val,
            'required_n': required_n,
        }

    # I) Render the template with all context
    return render(request, "growers/profile.html", {
        "farm_blocks":         farm_blocks,
        "recent_pest_checks":  recent_pest_checks,
        "status_filter":       status,
        "total_blocks":        total_blocks,
        "total_checks":        total_checks,
        "form":                form,
        "surveillance_result": surveillance_result,
        "sample_form":         sample_form,
        "sample_size_result":  sample_size_result,
    })


