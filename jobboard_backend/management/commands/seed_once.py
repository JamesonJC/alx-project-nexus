from django.core.management.base import BaseCommand
from django.core.management import call_command
from users.models import User  # Adjust based on your data

class Command(BaseCommand):
    help = 'Load initial fixture only if data not seeded'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write("Seeding initial data from fixture...")
            call_command('loaddata', 'initial_data.json')
        else:
            self.stdout.write("Initial data already seeded. Skipping.")

