from django.db import migrations


def make_bharath_superuser(apps, schema_editor):
    User = apps.get_model("auth", "User")

    User.objects.filter(username="Bharath").update(
        is_staff=True,
        is_superuser=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("jobportal", "0009_mocktestattempt_exam_and_more"),
    ]

    operations = [
        migrations.RunPython(make_bharath_superuser),
    ]