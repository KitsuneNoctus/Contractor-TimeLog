from django.urls import path
# from TimeLog.views import *
# from . import views, ClassCreateView
# from . import views
from TimeLog.views import ClassListView, ClassDetailView, ClassCreateView


urlpatterns = [
    path('', ClassListView.as_view(), name='class-list-page'),
    path('new/', ClassCreateView.as_view(), name='new'),
    path('<str:slug>/', ClassDetailView.as_view(), name='detail-page'),
    # path('new/', ClassCreateView.as_view(),name='new'),
]