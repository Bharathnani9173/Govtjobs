import json
from pathlib import Path

from django.apps import apps
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = "Import missing Exam records without overwriting existing records"

    def handle(self, *args, **options):
        path = Path.cwd() / "exams_export.json"

        if not path.exists():
            raise CommandError(f"Export file not found: {path}")

        try:
            with path.open(encoding="utf-8") as file:
                records = json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            raise CommandError(f"Could not read export file: {exc}") from exc

        Exam = apps.get_model("jobportal", "Exam")
        created = 0
        skipped = 0

        for record in records:
            if record.get("model") != "jobportal.exam":
                continue

            if Exam.objects.filter(pk=record.get("pk")).exists():
                skipped += 1
                continue

            try:
                objects = serializers.deserialize(
                    "json",
                    json.dumps([record]),
                    ignorenonexistent=True,
                )

                with transaction.atomic():
                    for obj in objects:
                        obj.save()
                        created += 1

            except Exception as exc:
                raise CommandError(
                    f"Failed to import Exam ID {record.get('pk')}: {exc}"
                ) from exc

        self.stdout.write(
            self.style.SUCCESS(
                f"Exam import finished. Created: {created}, Skipped: {skipped}"
            )
        )