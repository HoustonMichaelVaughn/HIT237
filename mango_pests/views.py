from django.shortcuts import render
from .data import Pestsdiseases

# Create your views here.

def home(request):
    
    return(render(request, 'mango_pests/home.html'))


def pestlist(request):
    #for x in range(2):
    #    pestcards.append({
    #    "text": "Mike Zebrowski is a figment of my imagination. It was the first royalty free image that I could find to use a temporary placeholder for images.",
    #   "title":"A wild Mike Zebrowski"})
    pestcards = []
    for pest in Pestsdiseases:
        pestcards.append(pest.dictionaryconstruct())
    return(render(request, 'mango_pests/project_list.html', {"pestcards": pestcards}))

def pest_detail(request, slugurl):
    for pest in Pestsdiseases:
        if(pest.urlslug == slugurl):
            pestdetails = pest.dictionaryconstruct()
            break
    for pest in pestdetails:
        print(pest)
    return(render(request, 'mango_pests/project_detail.html', {"pestdetails": pestdetails}))

def about(request):
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