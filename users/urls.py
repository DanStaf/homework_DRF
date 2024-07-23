from rest_framework import routers
from users.views import UserViewSet, PaymentListApiView
from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name

router_user = routers.DefaultRouter()
router_user.register("", UserViewSet, basename='user')

urlpatterns = [
    path('payments/', PaymentListApiView.as_view(), name='payment_list'),
]

urlpatterns += router_user.urls
