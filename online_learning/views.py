from django.shortcuts import render, get_object_or_404
from django.urls import path, include

from rest_framework import routers, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from online_learning.models import Course, Lesson, Subscription
from online_learning.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModeratorClass, IsOwnerClass


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModeratorClass]
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = [IsModeratorClass | IsOwnerClass]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwnerClass, ~IsModeratorClass]

        return super().get_permissions()

########


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModeratorClass]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerClass, ~IsModeratorClass]


class LessonRetrieveApiView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorClass | IsOwnerClass]


class LessonUpdateApiView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModeratorClass | IsOwnerClass]


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.all().filter(user=user).filter(course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка отключена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка включена'
        return Response({"message": message})
