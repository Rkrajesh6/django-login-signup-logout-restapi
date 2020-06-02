from django.shortcuts import render
from rest_framework.views import APIView
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics

# Create your views here.
class MyModelView(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer