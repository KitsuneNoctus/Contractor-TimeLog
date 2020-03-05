from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

from django.utils.text import slugify

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ClassForm

# Create your views here.
def home(request):
    classes = Class.objects.all()
    # return render
    # return('classes.html')
    context = {'classes':classes}
    return render(request,'classes.html', context)

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
    