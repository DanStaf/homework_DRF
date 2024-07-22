from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from online_learning.apps import OnlineLearningConfig
from rest_framework import routers
from online_learning.views import CourseViewSet

app_name = OnlineLearningConfig.name

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
