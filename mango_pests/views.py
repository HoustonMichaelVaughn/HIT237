from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest
from .data import Pestsdiseases, References
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PestCheck
from .forms import PestCheckForm
import re

# Sources
# https://docs.djangoproject.com/en/5.2/ref/request-response/
# https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint


def home(request):
    return render(request, "mango_pests/home.html")


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

class PestCheckListView(LoginRequiredMixin, ListView):
    model = PestCheck
    template_name = 'mango_pests/pestcheck_list.html'

    def get_queryset(self):
        return PestCheck.objects.filter(farm_block__grower=self.request.user)

class PestCheckCreateView(LoginRequiredMixin, CreateView):
    model = PestCheck
    form_class = PestCheckForm
    template_name = 'mango_pests/pestcheck_form.html'
    success_url = reverse_lazy('pestcheck_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form for queryset filtering
        return kwargs

    def form_valid(self, form):
        # Ensures the user owns the selected farm_block
        farm_block = form.cleaned_data['farm_block']
        if farm_block.grower != self.request.user:
            form.add_error('farm_block', 'You do not own this farm block.')
            return self.form_invalid(form)
        return super().form_valid(form)


class PestCheckUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PestCheck
    form_class = PestCheckForm
    template_name = 'mango_pests/pestcheck_form.html'
    success_url = reverse_lazy('pestcheck_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass user to limit farm_block choices
        return kwargs

    def test_func(self):
        pest_check = self.get_object()
        return pest_check.farm_block.grower == self.request.user

class PestCheckDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PestCheck
    template_name = 'mango_pests/pestcheck_confirm_delete.html'
    success_url = reverse_lazy('pestcheck_list')

    def test_func(self):
        pest_check = self.get_object()
        return pest_check.farm_block.grower == self.request.user