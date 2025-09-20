from django.db import models
from django.conf import settings
from categories.models import Category

# Create your models here.
class Job(models.Model):
    JOB_TYPES = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100, db_index=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        