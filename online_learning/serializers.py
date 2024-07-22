# from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from online_learning.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'owner']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'picture', 'course', 'owner']
        # fields = "__all__"
