# from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from online_learning.models import Course, Lesson
from rest_framework import serializers


class CourseSerializer(ModelSerializer):
    lessons_qty = serializers.SerializerMethodField(read_only=True)

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'owner', 'lessons_qty']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'picture', 'url', 'course', 'owner']
        # fields = "__all__"
