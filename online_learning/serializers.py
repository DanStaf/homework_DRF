# from django.contrib.auth.models import User
from rest_framework import serializers
from online_learning.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'owner']
