from django.shortcuts import render

# Create your views here.

def home(request):
    
    return(render(request, 'mango_pests\home.html'))

def about(request):

    return(render(request, r'mango_pests\about.html'))