#from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from jobs.models import Job, Category
from applications.models import Application

# Create your tests here.

User = get_user_model()

class TestApplicationView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass', role='user')
        self.admin = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.category = Category.objects.create(name='Health')
        self.job = Job.objects.create(
            title='Nurse',
            description='Health care',
            location='Lagos',
            job_type='contract',
            category=self.category,
            created_by=self.admin
        )

    def test_user_can_apply(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('application-list')
        data = {
            'job': self.job.id,
            'resume': 'https://resume.example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Application.objects.count(), 1)
