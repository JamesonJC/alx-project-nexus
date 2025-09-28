from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from categories.models import Category
from jobs.models import Job
from applications.models import Application
from users.models import Profile
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with initial sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # 1. Create users
        users = []
        for i in range(4):
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                email=f"user{i}@example.com"
            )
            if created:
                user.set_password("password123")
                user.save()
            users.append(user)

        self.stdout.write(f"Created {len(users)} users")

        # 2. Create categories
        category_names = ["Engineering", "Marketing", "Design", "Sales"]
        categories = []
        for name in category_names:
            cat, _ = Category.objects.get_or_create(name=name)
            categories.append(cat)

        self.stdout.write(f"Created {len(categories)} categories")

        # 3. Create jobs
        jobs = []
        for i in range(4):
            job, _ = Job.objects.get_or_create(
                title=f"Job Title {i}",
                description="Sample job description",
                location="Remote",
                job_type="Full-Time",
                category=random.choice(categories),
                created_by=random.choice(users)
            )
            jobs.append(job)

        self.stdout.write(f"Created {len(jobs)} jobs")

        # 4. Create applications
        for i in range(4):
            Application.objects.get_or_create(
                resume=f"resume_{i}.pdf",
                job=random.choice(jobs),
                applicant=random.choice(users),
                status=random.choice(["pending", "reviewed", "accepted", "rejected"])
            )

        self.stdout.write("Done seeding the database.")

