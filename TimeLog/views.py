from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
# Importing all models here
from .models import *

from django.utils.text import slugify

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ClassForm


class ClassListView(ListView):
    """ Renders a list of all Classes. """
    model = Class

    def get(self, request):
        """ GET a list of Classes. """
        classes = self.get_queryset().all()
        return render(request, 'classes.html', {
          'classes': classes
        })

class ClassDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Class

    def get(self, request, slug):
        """ Returns a specific Class page by slug. """
        s_class = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'class_detail.html', {
          's_class': s_class
        })
# ======================================================
# Create your views here.

# This is to ...
class ClassCreateView(CreateView):
    ''' '''
    def get(self, request, *args, **kwargs):
        context = {'form': ClassForm()}
        return render(request, 'new_class.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            page = form.save()
        return render(request, 'new.html', {'form': form})

#   def post(self, request, *args, **kwargs):
#       form = PageForm(request.POST)
#       if form.is_valid():
#           page = form.save(commit = False)
#           page.author = request.user
#           page.save()
#           # Using slugify here as the url takes in a string and not an Int id
#           return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[slugify(page.title)]))
#       return render(request, 'new.html', {'form': form})
    