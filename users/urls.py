from rest_framework import routers
from users.views import UserViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

router_user = routers.DefaultRouter()
router_user.register("", UserViewSet, basename='user')

urlpatterns = []
urlpatterns += router_user.urls
