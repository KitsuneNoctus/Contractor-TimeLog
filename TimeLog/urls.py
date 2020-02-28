from django.urls import path
from TimeLog.views import *


urlpatterns = [
    path('classes.html', views.home),
    # path('', PageListView.as_view(), name='wiki-list-page'),
    # path('new/', PageCreateView.as_view(),name='new'),
    # path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]