from django.views.generic import TemplateView
#class based view is imported to render templates
from.data import Pestdiseases
#imports data from Pestdiseases
class HomeView(TemplateView):
  template_name = 'mango_pests/home.html' 
  #create class HomeView to render the HomePage from template home.html
class PestListView(TemplateView):
  template_name = 'mango_pests/project_list.html'
  #create class PestListView to render the Pest List Page from template project_list.html
    def get_context_data(self,**kwargs):
      # define method get_context_data to apply PestListView to data that is input through the template project_list.html
      context = super(). get_context_data(**kwargs)
      #allows additional arguments to be accepted by context dictionary
      context['pestcards']=[pest.dictionaryconstruct()] for pest in Pestdiseases]
      return context
      
      
