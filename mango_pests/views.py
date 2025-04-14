from django.shortcuts import render
from .data import Pestsdiseases
from django.views import View

# Create your views here.

def home(request):
    return(render(request, 'mango_pests/home.html'))

class PestListView(View):
    def get(self, request):
        pestcards = [pest.dictionaryconstruct() for pest in Pestsdiseases]
        return(render(request, 'mango_pests/project_list.html', {"pestcards": pestcards}))

class PestDetailView(View):
    def get(self, request, slugurl):
        for pest in Pestsdiseases:
            if(pest.urlslug == slugurl):
                pestdetails = pest.__dict__
                break
        return(render(request, 'mango_pests/project_detail.html', {"pestdetails": pestdetails}))

class AboutView(View):
    def get(self, request):
        aboutcards = [
            {"membername":"Houston Vaughn",
                "aboutmember":"A computer science student at CDU. Teamleader for Group 7"},
            {"membername":"Neolisa De Castro",
                "aboutmember":"Temp Text"},
            {"membername":"Gislene Freitas De Lima Clancy",
                "aboutmember":"Temp Text"},
            {"membername":"Dean Metcalfe",
                "aboutmember":"Temp Text"}
            ]
        return(render(request, r'mango_pests\about.html',{"aboutcards":aboutcards}))