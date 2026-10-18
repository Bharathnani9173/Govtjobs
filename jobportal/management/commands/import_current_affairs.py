
import json
from datetime import date
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from jobportal.models import CurrentAffair, Job


class Command(BaseCommand):
    help = "Import Current Affairs records from a custom UTF-8 JSON file"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        file_path = Path(options["json_file"])

        if not file_path.is_file():
            raise CommandError(f"File not found: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise CommandError("Expected a JSON list of records.")

        created = 0
        skipped = 0

        with transaction.atomic():
            for item in records:
                job = None

                # Do not assume local Job IDs match production IDs.
                # Preserve the relationship only if a matching job exists.
                job_id = item.get("job_id")
                if job_id:
                    job = Job.objects.filter(pk=job_id).first()

                # Avoid duplicates using the record's identifying content.
                exists = CurrentAffair.objects.filter(
                    period=item["period"],
                    title=item["title"],
                    date=date.fromisoformat(item["date"]),
                ).exists()

                if exists:
                    skipped += 1
                    continue

                CurrentAffair.objects.create(
                    period=item["period"],
                    title=item["title"],
                    title_te=item.get("title_te", ""),
                    category=item["category"],
                    date=date.fromisoformat(item["date"]),
                    description=item["description"],
                    description_te=item.get("description_te", ""),
                    pdf_link=item.get("pdf_link", ""),
                    job=job,
                )
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished. Created: {created}, Skipped: {skipped}"
            )
        )
