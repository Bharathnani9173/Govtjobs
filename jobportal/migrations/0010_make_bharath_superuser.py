from django.db import migrations
from django.contrib.auth.hashers import make_password


def make_bharath_superuser(apps, schema_editor):
    User = apps.get_model("auth", "User")

    user, created = User.objects.get_or_create(
        username="Bharath",
        defaults={
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )

    if not created:
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("jobportal", "0009_mocktestattempt_exam_and_more"),
    ]

    operations = [
        migrations.RunPython(make_bharath_superuser),
    ]