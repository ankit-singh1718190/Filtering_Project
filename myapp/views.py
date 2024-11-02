from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['city']  
