import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from jobportal.models import Exam, ExamPattern


class Command(BaseCommand):
    help = "Import exam patterns from exam_patterns_export.json"

    def handle(self, *args, **options):
        file_path = Path("exam_patterns_export.json")

        if not file_path.exists():
            raise CommandError(
                "exam_patterns_export.json was not found in the project root."
            )

        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        created = 0
        updated = 0
        skipped = 0

        with transaction.atomic():
            for item in data:
                exam = Exam.objects.filter(
                    name=item["exam"]
                ).first()

                if exam is None:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Skipped: exam not found — {item['exam']}"
                        )
                    )
                    skipped += 1
                    continue

                pattern, was_created = ExamPattern.objects.update_or_create(
                    exam=exam,
                    subject=item["subject"],
                    defaults={
                        "question_count": item["question_count"],
                        "duration_minutes": item["duration_minutes"],
                        "marks_per_question": item["marks_per_question"],
                        "negative_marking": item["negative_marking"],
                    },
                )

                if was_created:
                    created += 1
                else:
                    updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished. Created: {created}, "
                f"Updated: {updated}, Skipped: {skipped}, "
                f"Total in file: {len(data)}"
            )
        )
