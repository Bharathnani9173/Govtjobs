
import json
from pathlib import Path

from django.apps import apps
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = "Import previous papers without overwriting existing records"

    def handle(self, *args, **options):
        fixture_path = Path.cwd() / "previous_papers_export.json"

        if not fixture_path.exists():
            raise CommandError(f"Export file not found: {fixture_path}")

        try:
            with fixture_path.open(encoding="utf-8") as file:
                records = json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            raise CommandError(f"Could not read export file: {exc}") from exc

        PreviousPaper = apps.get_model("jobportal", "PreviousPaper")
        created = 0
        skipped = 0
        failed = 0

        for record in records:
            if record.get("model") != "jobportal.previouspaper":
                continue

            pk = record.get("pk")

            if PreviousPaper.objects.filter(pk=pk).exists():
                skipped += 1
                continue

            try:
                objects = serializers.deserialize(
                    "json",
                    json.dumps([record]),
                    ignorenonexistent=True,
                )

                for obj in objects:
                    paper = obj.object
                    missing_relation = None

                    for field in paper._meta.fields:
                        if not field.is_relation:
                            continue

                        related_id = getattr(paper, field.attname, None)

                        if related_id is None:
                            continue

                        related_model = field.remote_field.model

                        if not related_model.objects.filter(
                            pk=related_id
                        ).exists():
                            missing_relation = (field.name, related_id)
                            break

                    if missing_relation:
                        field_name, related_id = missing_relation
                        self.stdout.write(
                            self.style.WARNING(
                                f"Skipping paper {pk}: missing "
                                f"{field_name} ID {related_id}"
                            )
                        )
                        skipped += 1
                        continue

                    with transaction.atomic():
                        obj.save()

                    created += 1

            except Exception as exc:
                failed += 1
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed to import paper {pk}: {exc}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished. Created: {created}, "
                f"Skipped: {skipped}, Failed: {failed}"
            )
        )
