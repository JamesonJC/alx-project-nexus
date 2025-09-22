from django.test import TestCase
from jobs.models import Job, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class TestJobModels(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.category = Category.objects.create(name='Finance')
        self.job = Job.objects.create(
            title='Financial Analyst',
            description='Analyze financial data',
            location='NYC',
            job_type='full-time',
            category=self.category,
            created_by=self.admin
        )

    def test_job_str_returns_title(self):
        self.assertEqual(str(self.job), 'Financial Analyst')

    def test_job_category(self):
        self.assertEqual(self.job.category.name, 'Finance')
