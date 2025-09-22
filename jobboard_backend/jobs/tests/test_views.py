#from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from jobs.models import Job, Category

# Create your tests here.

User = get_user_model()

class TestJobView(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.user = User.objects.create_user(username='user', password='userpass', role='user')
        self.category = Category.objects.create(name='Tech')
        self.job_data = {
            'title': 'Django Dev',
            'description': 'Build APIs',
            'location': 'Remote',
            'job_type': 'full-time',
            'category': self.category.id
        }

    def test_admin_can_create_job(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('job-list')
        response = self.client.post(url, self.job_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Job.objects.count(), 1)

    def test_user_cannot_create_job(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('job-list')
        response = self.client.post(url, self.job_data)
        self.assertEqual(response.status_code, 403)
