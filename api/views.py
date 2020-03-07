from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from TimeLog.models import Class
from api.serializers import ClassSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView


class ClassList(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # def get(self, request):
    #     classes = Class.objects.all()[:20]
    #     data = ClassSerializer(classes, many=True).data
    #     return Response(data)

class ClassDetail(RetrieveDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # def get(self, request, pk):
    #     clas = get_object_or_404(Class, pk=pk)
    #     data = ClassSerializer(clas).data
    #     return Response(data)

