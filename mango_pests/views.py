from django.shortcuts import render

# Create your views here.

def home(request):
    
    return(render(request, 'mango_pests\home.html'))

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