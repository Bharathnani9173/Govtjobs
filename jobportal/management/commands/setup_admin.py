from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = "Create or update the Render admin superuser"

    def handle(self, *args, **options):

        username = "pBharath"

        # Get password from Render Environment Variable
        password = os.environ.get("DJANGO_ADMIN_PASSWORD")

        if not password:
            self.stdout.write(
                self.style.ERROR(
                    "DJANGO_ADMIN_PASSWORD environment variable is missing."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created superuser: {username}"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Updated superuser: {username}"
                )
            )