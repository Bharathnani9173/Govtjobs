import json
import os
from django.db import migrations
from django.conf import settings


def import_ssc_cgl_questions(apps, schema_editor):
    MockTestQuestion = apps.get_model('jobportal', 'MockTestQuestion')

    fixture_path = os.path.join(
        settings.BASE_DIR, 'jobportal', 'data', 'ssc_cgl_fixture.json'
    )

    if not os.path.exists(fixture_path):
        print(f"Fixture not found at {fixture_path}, skipping import.")
        return

    with open(fixture_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    created_count = 0
    for q in questions:
        obj, created = MockTestQuestion.objects.get_or_create(
            question=q['question'],
            exam_name=q.get('exam_name', ''),
            defaults={
                'exam': q.get('exam', ''),
                'subject': q.get('subject', ''),
                'option1': q.get('option1', ''),
                'option2': q.get('option2', ''),
                'option3': q.get('option3', ''),
                'option4': q.get('option4', ''),
                'answer': q.get('answer', ''),
                'explanation': q.get('explanation', ''),
                'difficulty': q.get('difficulty', ''),
                'source': q.get('source', ''),
                'is_active': q.get('is_active', True),
            }
        )
        if created:
            created_count += 1

    print(f"Imported {created_count} new SSC CGL questions (skipped existing).")


def reverse_noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0010_make_bharath_superuser'),
    ]

    operations = [
        migrations.RunPython(import_ssc_cgl_questions, reverse_noop),
    ]
    