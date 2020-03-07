from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
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
        clas = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'class_detail.html', {
          'clas': clas
        })
# ======================================================
# Create your views here.
class ClassCreateView(CreateView):
    ''' '''
    def get(self, request, *args, **kwargs):
        context = {'form': ClassForm()}
        return render(request, 'new_class.html', context)

    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            clas = form.save(commit = False)
            #   clas.author = request.user
            clas.save()
            # Using slugify here as the url takes in a string and not an Int id
            return HttpResponseRedirect(reverse_lazy('detail-page', args=[slugify(clas.class_name)]))
        return render(request, 'new.html', {'form': form})
    