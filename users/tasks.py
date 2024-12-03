import datetime
from django.utils import timezone

from celery import shared_task
from users.models import User


@shared_task
def check_users_last_login():

    dt_now = timezone.now()
    dt_one_month_earlier = dt_now - datetime.timedelta(days=30)

    users = User.objects.all()

    for user in users:
        if user.is_active:
            if user.last_login is None or user.last_login <= dt_one_month_earlier:
                user.is_active = False
                user.save()
                print(user, user.last_login, user.is_active)

    print("#")
