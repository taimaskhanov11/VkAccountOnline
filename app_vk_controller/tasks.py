from celery import shared_task


@shared_task
def BIG(x, y):
    return x ** y
