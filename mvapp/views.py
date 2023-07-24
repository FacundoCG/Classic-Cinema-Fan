from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Gender, Company, Movie
#__________
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#________
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
#________
from .forms import MovieForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "mvapp/home.html"
    
class MovieList(ListView):
    model = Movie

@method_decorator(staff_member_required, name="dispatch")     
class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movie-list')

@method_decorator(staff_member_required, name="dispatch")      
class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('movie-update', args=[self.object.id]) + '?ok'   

@method_decorator(staff_member_required, name="dispatch")      
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-list')