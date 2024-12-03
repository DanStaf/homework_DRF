from celery import shared_task


@shared_task
def my_task(x, y):
    return print("Hello")
