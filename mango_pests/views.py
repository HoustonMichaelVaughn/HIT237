from django.shortcuts import render

# Create your views here.

def home(request):
    
    return(render(request, 'mango_pests\home.html'))

def pestlist(request):
    pestcards = [
        {"image":"https://upload.wikimedia.org/wikipedia/en/6/6a/Mike_Wazowski.png",
        "text": "Mike Wazowski is a major character in Monsters, Inc. and Monsters University, produced by Pixar Animation Studios. He is a small, round, green monster with one large eye, short limbs, and tiny horns on his head.",
        "title":"A wild mike wazowski"},
        {"image":"https://upload.wikimedia.org/wikipedia/en/6/6a/Mike_Wazowski.png",
        "text": "Mike Wazowski is a major character in Monsters, Inc. and Monsters University, produced by Pixar Animation Studios. He is a small, round, green monster with one large eye, short limbs, and tiny horns on his head.",
        "title":"A wild mike wazowski"},
    ]
    return(render(request, 'mango_pests\project_list.html', {"pestcards":pestcards}))

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