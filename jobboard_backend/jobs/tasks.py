from celery import shared_task
from .models import Job

@shared_task
def notify_user(email):
    print(f"Sending notification to {email}")

@shared_task
def notify_new_job(job_id):
    try:
        job = Job.objects.get(id=job_id)
        print(f"[Celery] New job posted: {job.title}")
        
        # You can also call notify_user here, for example:
        # notify_user.delay("admin@example.com")

    except Job.DoesNotExist:
        print(f"[Celery] Job with ID {job_id} does not exist.")
