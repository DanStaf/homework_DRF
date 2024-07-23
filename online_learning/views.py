from django.shortcuts import render
from django.urls import path, include

from rest_framework import routers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from online_learning.models import Course, Lesson
from online_learning.serializers import CourseSerializer, LessonSerializer
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
