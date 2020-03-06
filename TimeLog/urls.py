from django.urls import path
# from TimeLog.views import *
# from . import views, ClassCreateView
# from . import views
# from TimeLog.views import ClassListView, ClassDetailView
from TimeLog.views import ClassListView


urlpatterns = [
    path('', ClassListView.as_view(), name='class-list-page'),
    # path('', views.home),
    # path('new/', ClassCreateView.as_view(),name='new'),
]