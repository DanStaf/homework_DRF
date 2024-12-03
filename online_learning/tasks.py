from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from online_learning.models import Subscription, Course


@shared_task
def send_updates_to_users(course_pk):
    """
    :param course_pk: для передачи объекта course нужно изменить settings.py, добавить
    #CELERY_ACCEPT_CONTENT = ['pickle', 'json']
    #CELERY_TASK_SERIALIZER = 'pickle'
    #CELERY_RESULT_SERIALIZER = 'pickle'

    :return:
    """

    course = Course.objects.filter(pk=course_pk).first()

    subject = f"Курс '{course}' обновился!"
    message = subject

    recipient_list = [item.user.email for item in Subscription.objects.filter(course=course)]

    if recipient_list:
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list
        )
