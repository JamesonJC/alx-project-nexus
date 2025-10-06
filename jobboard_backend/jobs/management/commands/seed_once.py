from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from jobs.models import Job
from applications.models import Application
from categories.models import Category

User = get_user_model()

class Command(BaseCommand):
    help = 'Fully reset and seed the database with categories, jobs, and applications'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting old data..."))

        Application.objects.all().delete()
        Job.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Old data cleared.")

        # Get the existing admin user
        try:
            admin = User.objects.get(username="admin")
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Admin user not found. Make sure 'admin' exists."))
            return

        self.stdout.write("Found admin user.")

        # Create categories
        categories = ["Engineering", "Design", "Marketing", "Sales"]
        created_categories = []
        for name in categories:
            cat = Category.objects.create(name=name)
            created_categories.append(cat)

        self.stdout.write("Categories created.")

        # Create jobs
        for i, category in enumerate(created_categories):
            job = Job.objects.create(
                title=f"{category.name} Job {i+1}",
                description="This is a sample job for seeding.",
                location="Remote",
                job_type="full-time",
                category=category,
                created_by=admin,
            )
            self.stdout.write(f"Created job: {job.title}")

        # Create applications for the first job
        first_job = Job.objects.first()
        if first_job:
            Application.objects.create(
                job=first_job,
                applicant=admin,
                resume="This is a seeded application by admin.",
                status="pending"
            )
            self.stdout.write("Created sample application for the first job.")

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully."))
