from django.shortcuts import render
from .data import Pestsdiseases
from django.views import View

# Create your views here.

def home(request):
    return(render(request, 'mango_pests/home.html'))

class PestListView(View):
    def get(self, request):
        pestcards = [pest.__dict__ for pest in Pestsdiseases]
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
                "aboutmember":"Computer Science Student."},
            {"membername":"Gislene Freitas De Lima Clancy",
                "aboutmember":"A computer science student at CDU."},
            {"membername":"Dean Metcalfe",
                "aboutmember":"A computer science student at CDU."}
            ]
        return(render(request, r'mango_pests\about.html',{"aboutcards":aboutcards}))
#class ReferencesView(TemplateView):
    # Set the template to render as 'mango_pests/references.html'
#   template_name = 'mango_pests/references.html'
