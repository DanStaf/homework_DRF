import stripe

from config.settings import STRIPE_API_KEY

"""import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule"""


stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):

    title = f"{instance.course}" if instance.course else f"{instance.lesson}"
    return stripe.Product.create(name=title)


def create_stripe_price(product, amount):

    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=product.get("id")
    )


def create_stripe_session(price, success_url):

    return stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )


def get_stripe_session_retrieve(session_id):

    response = stripe.checkout.Session.retrieve(session_id, )
    return response.get("status")

"""
######## PeriodicTask

def set_schedule():

    # Создаем интервал для повтора
    schedule, created = IntervalSchedule.objects.get_or_create(
         every=10,
         period=IntervalSchedule.SECONDS,
     )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
         interval=schedule,
         name='Importing contacts',
         task='proj.tasks.import_contacts',
         args=json.dumps(['arg1', 'arg2']),
         kwargs=json.dumps({
            'be_careful': True,
         }),
         expires=datetime.utcnow() + timedelta(seconds=30)
     )
"""
