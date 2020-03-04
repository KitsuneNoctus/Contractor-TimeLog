from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    classes = Class.objects.all()
    # return render
    # return('classes.html')
    context = {'classes':classes}
    return render(request,'classes.html', context)
    