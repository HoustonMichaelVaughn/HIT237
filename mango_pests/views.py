from django.shortcuts import render
from django.http import HttpRequest
from .data import Pestsdiseases, References
from django.views import View
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
