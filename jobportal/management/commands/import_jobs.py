
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.apps import apps


class Command(BaseCommand):
    help = "Safely import exported jobs without overwriting existing job IDs"

    def handle(self, *args, **options):
        project_root = Path.cwd()
        fixture_path = project_root / "jobs_export.json"

        if not fixture_path.exists():
            raise CommandError(f"Export file not found: {fixture_path}")

        with fixture_path.open(encoding="utf-8") as file:
            records = json.load(file)

        Job = apps.get_model("jobportal", "Job")
        created = 0
        skipped = 0

        with transaction.atomic():
            for record in records:
                if record.get("model") != "jobportal.job":
                    continue

                pk = record.get("pk")
                fields = record.get("fields", {})

                if Job.objects.filter(pk=pk).exists():
                    skipped += 1
                    continue

                Job.objects.create(pk=pk, **fields)
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete. Created: {created}, Skipped existing IDs: {skipped}"
            )
        )
