import datetime
from django.core.management import BaseCommand
from online_learning.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = [item for item in User.objects.all()]
        courses = [item for item in Course.objects.all()]
        lessons = [item for item in Lesson.objects.all()]

        payment = Payment.objects.create(
            owner=users[2],
            payment_date=datetime.datetime.now(),
            course=courses[1],
            # lesson =
            value=1000,
            payment_method=Payment.CASH
        )
        payment.save()

        payment1 = Payment.objects.create(
            owner=users[1],
            payment_date=datetime.datetime.now(),
            # course=courses[1],
            lesson=lessons[1],
            value=100,
            payment_method=Payment.CARD
        )
        payment1.save()

        payment2 = Payment.objects.create(
            owner=users[2],
            payment_date=datetime.datetime.now(),
            # course=courses[1],
            lesson=lessons[2],
            value=200,
            payment_method=Payment.CARD
        )
        payment2.save()
