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

        with fixture_path.open(encoding="utf-8") as file:
            records = json.load(file)

        PreviousPaper = apps.get_model("jobportal", "PreviousPaper")
        created = 0
        skipped = 0

        with transaction.atomic():
            for record in records:
                if record.get("model") != "jobportal.previouspaper":
                    continue

                pk = record.get("pk")

                if PreviousPaper.objects.filter(pk=pk).exists():
                    skipped += 1
                    continue

                objects = serializers.deserialize(
                    "json",
                    json.dumps([record]),
                    ignorenonexistent=True,
                )

                for obj in objects:
                    paper = obj.object
                    missing_relation = False

                    for field in paper._meta.fields:
                        if not field.is_relation or field.null:
                            continue

                        related_id = getattr(paper, field.attname, None)

                        if related_id is None:
                            continue

                        related_model = field.remote_field.model

                        if not related_model.objects.filter(
                            pk=related_id
                        ).exists():
                            self.stdout.write(
                                f"Skipping paper {paper.pk}: "
                                f"missing {field.name} ID {related_id}"
                            )
                            missing_relation = True
                            break

                    if missing_relation:
                        skipped += 1
                        continue

                    obj.save()
                    created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import complete. Created: {created}, "
                f"Skipped: {skipped}"
            )
        )