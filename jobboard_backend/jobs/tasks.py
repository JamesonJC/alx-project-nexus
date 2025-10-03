from celery import shared_task

@shared_task
def notify_user(email):
    print(f"Sending notification to {email}")
