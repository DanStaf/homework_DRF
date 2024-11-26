from django.urls import path, include
from online_learning.apps import OnlineLearningConfig
from rest_framework import routers
from online_learning.views import CourseViewSet, LessonListApiView, LessonRetrieveApiView, LessonCreateApiView, \
    LessonDestroyApiView, LessonUpdateApiView, SubscriptionAPIView

app_name = OnlineLearningConfig.name

router_course = routers.DefaultRouter()
router_course.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router_course.urls)),

    path('lessons/', LessonListApiView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson'),
    path('lessons/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/delete/', LessonDestroyApiView.as_view(), name='lesson_delete'),
    path('lessons/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),

    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
]
