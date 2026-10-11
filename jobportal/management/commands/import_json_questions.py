import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from jobportal.models import Exam, QuizQuestion


class Command(BaseCommand):
    help = "Import JSON question banks into QuizQuestion"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            required=True,
            help="JSON file name inside jobportal/question_banks/"
        )

    def handle(self, *args, **options):

        filename = options["file"]

        bank_dir = (
            Path(settings.BASE_DIR)
            / "jobportal"
            / "question_banks"
        )

        json_file = bank_dir / filename

        if not json_file.exists():
            raise CommandError(
                f"File not found: {json_file}"
            )

        try:
            with open(
                json_file,
                "r",
                encoding="utf-8-sig"
            ) as f:
                data = json.load(f)

        except json.JSONDecodeError as e:
            raise CommandError(
                f"Invalid JSON: {e}"
            )

        # -----------------------------------------
        # SUPPORT MULTIPLE JSON FORMATS
        # -----------------------------------------

        exam_name = None

        # Format:
        # {
        #   "exam": "District Court",
        #   "questions": [...]
        # }
        if isinstance(data, dict):

            exam_name = data.get("exam")

            questions_data = data.get(
                "questions",
                []
            )

        # Format:
        # [
        #   {
        #       "exam_name": "Telangana AEE",
        #       ...
        #   }
        # ]
        elif isinstance(data, list):

            questions_data = data

        else:
            raise CommandError(
                "Unsupported JSON format."
            )

        if not isinstance(questions_data, list):
            raise CommandError(
                "Questions must be stored in a list."
            )

        if not questions_data:
            raise CommandError(
                "No questions found in JSON file."
            )

        # -----------------------------------------
        # GET EXAM NAME
        # -----------------------------------------

        if not exam_name:

            exam_name = questions_data[0].get(
                "exam_name"
            )

        if not exam_name:
            raise CommandError(
                "Exam name could not be found in JSON."
            )

        # -----------------------------------------
        # FIND EXAM
        # -----------------------------------------

        exam = Exam.objects.filter(
            name=exam_name
        ).first()

        if not exam:
            raise CommandError(
                f'Exam "{exam_name}" not found in database.'
            )

        added = 0
        skipped = 0

        # -----------------------------------------
        # IMPORT QUESTIONS
        # -----------------------------------------

        for item in questions_data:

            question_text = str(
                item.get("question", "")
            ).strip()

            if not question_text:
                skipped += 1
                continue

            # Prevent duplicates
            exists = QuizQuestion.objects.filter(
                exam=exam,
                question=question_text
            ).exists()

            if exists:
                skipped += 1
                continue

            QuizQuestion.objects.create(

                exam=exam,

                job=None,

                question=question_text,

                option1=str(
                    item.get("option1", "")
                ).strip(),

                option2=str(
                    item.get("option2", "")
                ).strip(),

                option3=str(
                    item.get("option3", "")
                ).strip(),

                option4=str(
                    item.get("option4", "")
                ).strip(),

                answer=str(
                    item.get("answer", "")
                ).strip(),

                subject=str(
                    item.get(
                        "subject",
                        "General"
                    )
                ).strip(),

                difficulty=str(
                    item.get(
                        "difficulty",
                        "Medium"
                    )
                ).strip(),

                source=str(
                    item.get(
                        "source",
                        "Practice"
                    )
                ).strip(),
            )

            added += 1

        # -----------------------------------------
        # RESULT
        # -----------------------------------------

        self.stdout.write(
            self.style.SUCCESS(
                f"Exam: {exam.name}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Questions added: {added}"
            )
        )

        self.stdout.write(
            self.style.WARNING(
                f"Questions skipped: {skipped}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Import completed."
            )
        )