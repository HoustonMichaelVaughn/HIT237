from django.shortcuts import render

# Create your views here.

def home(request):
    
    return(render(request, 'mango_pests\home.html'))

def pestlist(request):
    pestcards = []
    for x in range(2):
        pestcards.append({
        "text": "Mike Zebrowski is a figment of my imagination. It was the first royalty free image that I could find to use a temporary placeholder for images.",
        "title":"A wild Mike Zebrowski"})
    return(render(request, 'mango_pests\project_list.html', {"pestcards":pestcards}))

def pestlist_about(request):

    return(render(request, 'mango_pests\project_detail.html'))

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