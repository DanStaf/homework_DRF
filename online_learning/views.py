from django.shortcuts import render
from django.urls import path, include

from rest_framework import routers, viewsets
from online_learning.models import Course
from online_learning.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
