import json
from pathlib import Path

from django.apps import apps
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = "Import missing quiz questions without overwriting existing records"

    def handle(self, *args, **options):
        path = Path.cwd() / "quiz_questions_export.json"

        if not path.exists():
            raise CommandError(f"Export file not found: {path}")

        try:
            with path.open(encoding="utf-8") as file:
                records = json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            raise CommandError(f"Could not read export file: {exc}") from exc

        QuizQuestion = apps.get_model("jobportal", "QuizQuestion")
        created = 0
        skipped = 0

        for record in records:
            if record.get("model") != "jobportal.quizquestion":
                continue

            pk = record.get("pk")

            if QuizQuestion.objects.filter(pk=pk).exists():
                skipped += 1
                continue

            try:
                objects = serializers.deserialize(
                    "json",
                    json.dumps([record], ensure_ascii=False),
                    ignorenonexistent=True,
                )

                with transaction.atomic():
                    for obj in objects:
                        question = obj.object
                        missing_relation = None

                        for field in question._meta.fields:
                            if not field.is_relation:
                                continue

                            related_id = getattr(question, field.attname, None)
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
                            skipped += 1
                            self.stdout.write(
                                f"Skipped question {pk}: missing "
                                f"{field_name} ID {related_id}"
                            )
                            continue

                        obj.save()
                        created += 1

            except Exception as exc:
                raise CommandError(
                    f"Failed to import question {pk}: {exc}"
                ) from exc

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished. Created: {created}, Skipped: {skipped}"
            )
        )
