
import csv
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from jobportal.models import Exam, MockTestQuestion


class Command(BaseCommand):
    help = "Import exam-wise mock test questions from CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default="jobportal/data/mock_questions.csv",
            help="Path to CSV file",
        )

    def handle(self, *args, **options):
        csv_file = Path(options["file"])

        if not csv_file.exists():
            raise CommandError(
                f"CSV file not found: {csv_file}"
            )

        required_columns = {
            "exam_name",
            "subject",
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
            "explanation",
            "difficulty",
            "source",
        }

        created = 0
        updated = 0
        skipped = 0

        with csv_file.open(
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            if not reader.fieldnames:
                raise CommandError("CSV has no header row.")

            missing = required_columns - set(reader.fieldnames)

            if missing:
                raise CommandError(
                    "Missing columns: "
                    + ", ".join(sorted(missing))
                )

            for row_number, row in enumerate(
                reader,
                start=2
            ):

                exam_name = row["exam_name"].strip()
                subject = row["subject"].strip()
                question = row["question"].strip()

                if not exam_name or not question:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Row {row_number}: "
                            "missing exam_name or question. Skipped."
                        )
                    )
                    skipped += 1
                    continue

                # -----------------------------------------
                # FIND EXAM
                # -----------------------------------------

                try:
                    exam = Exam.objects.get(
                        name__iexact=exam_name
                    )
                except Exam.DoesNotExist:

                    self.stdout.write(
                        self.style.ERROR(
                            f"Row {row_number}: "
                            f"Exam '{exam_name}' not found. "
                            "Skipped."
                        )
                    )

                    skipped += 1
                    continue

                # -----------------------------------------
                # CHECK DUPLICATE QUESTION
                # -----------------------------------------

                existing = MockTestQuestion.objects.filter(
                    exam=exam,
                    question=question
                ).first()

                data = {
                    "exam": exam,
                    "exam_name": exam.name,
                    "subject": subject,
                    "option1": row["option1"].strip(),
                    "option2": row["option2"].strip(),
                    "option3": row["option3"].strip(),
                    "option4": row["option4"].strip(),
                    "answer": row["answer"].strip(),
                    "explanation": row["explanation"].strip(),
                    "difficulty": (
                        row["difficulty"].strip()
                        or "Medium"
                    ),
                    "source": row["source"].strip(),
                    "is_active": True,
                }

                # -----------------------------------------
                # UPDATE EXISTING
                # -----------------------------------------

                if existing:

                    for field, value in data.items():
                        setattr(
                            existing,
                            field,
                            value
                        )

                    existing.save()

                    updated += 1

                # -----------------------------------------
                # CREATE NEW
                # -----------------------------------------

                else:

                    MockTestQuestion.objects.create(
                        question=question,
                        **data
                    )

                    created += 1

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "======================================"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "MOCK QUESTION IMPORT COMPLETED"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "======================================"
            )
        )

        self.stdout.write(
            f"Created : {created}"
        )

        self.stdout.write(
            f"Updated : {updated}"
        )

        self.stdout.write(
            f"Skipped : {skipped}"
        )
