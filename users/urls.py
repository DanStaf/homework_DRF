from rest_framework import routers
from rest_framework.permissions import AllowAny

from users.views import UserViewSet, PaymentListApiView, UserCreateApiView
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router_user = routers.DefaultRouter()
router_user.register("", UserViewSet, basename='user')

urlpatterns = [
    path('payments/', PaymentListApiView.as_view(), name='payment_list'),

    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router_user.urls

