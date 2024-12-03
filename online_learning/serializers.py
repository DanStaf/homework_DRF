# from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from online_learning.models import Course, Lesson, Subscription
from rest_framework import serializers

from online_learning.validators import TextValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'picture', 'url', 'course', 'owner']
        validators = [TextValidator(field='url', correct_text='youtube.com')]

        # fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons_qty = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(read_only=True, many=True, source='lesson_set')
    is_user_signed = serializers.SerializerMethodField(read_only=True)

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    def get_is_user_signed(self, obj):
        subs = Subscription.objects.filter(course=obj).filter(user=self.context["request"].user)
        return subs.exists()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'picture', 'owner', 'is_user_signed', 'lessons_qty', 'lessons']


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
