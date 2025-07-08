from celery import shared_task


@shared_task
def send_email(emil):
    print("hello ", emil)
