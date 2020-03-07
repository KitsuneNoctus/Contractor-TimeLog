from django.urls import path

from api.views import ClassList, ClassDetail

urlpatterns = [
    path('class/', ClassList.as_view(), name='class_list'),
    path('class/<int:pk>', ClassDetail.as_view(), name='class_detail')
]