from django.urls import path
# from TimeLog.views import *
from . import views


urlpatterns = [
    # path('',views.home,name='home'),
    path('classes.html', views.home),
]