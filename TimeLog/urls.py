from django.urls import path
# from TimeLog.views import *
# from . import views, ClassCreateView
from . import views


urlpatterns = [
    path('', views.home),
    # path('new/', ClassCreateView.as_view(),name='new'),
]