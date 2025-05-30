from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from mango_pests.models import FarmBlock, PestCheck
from .forms import RegisterUserForm
from mango_pests.forms import PestSelectionForm, SampleSizeForm  # Ensure SampleSizeForm is in your forms because this form class is what renders and processes the “How Many Trees Should I Check?” calculator

import math

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
    #  All farm blocks and pest checks for this user
    farm_blocks = FarmBlock.objects.filter(grower=request.user)
    all_checks  = PestCheck.objects.filter(
        farm_block__grower=request.user
    ).order_by('-date_checked')

    # Status filter via ?status=
    status = request.GET.get("status", "all")
    if status == "high":
        all_checks = all_checks.filter(confidence__gte=0.9)
    elif status == "medium":
        all_checks = all_checks.filter(confidence__gte=0.5, confidence__lt=0.9)
    elif status == "low":
        all_checks = all_checks.filter(confidence__lt=0.5)

    # Totals for summary cards
    total_blocks = farm_blocks.count()
    total_checks = all_checks.count()

    #  Keep only the 5 most recent for the table
    recent_pest_checks = all_checks[:5]

    # Two separate forms with different prefixes
    form = PestSelectionForm(request.POST or None, prefix='surv')
    sample_form = SampleSizeForm(request.POST or None, prefix='sample')

    surveillance_result = None
    sample_size_result = None

    # Determine which form was submitted
    if 'surv-pest' in request.POST and form.is_valid():
        pest = form.cleaned_data['pest']
        checks = PestCheck.objects.filter(
            pest=pest,
            positives=0,
            farm_block__grower=request.user
        )
        total_checked = sum(c.num_trees_checked for c in checks)
        confidence = 100 * (1 - (1 - 0.01) ** total_checked) if total_checked > 0 else None
        surveillance_result = {
            'pest': pest,
            'total_checked': total_checked,
            'confidence': confidence,
        }

    if 'sample-prevalence' in request.POST and sample_form.is_valid():
        p = sample_form.cleaned_data['prevalence']
        c = sample_form.cleaned_data['confidence']
        required_n = math.ceil(math.log(1 - c) / math.log(1 - p))
        sample_size_result = {
            'prevalence': p,
            'confidence': c,
            'required_n': required_n,
        }

    # computing sample_size_result
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


