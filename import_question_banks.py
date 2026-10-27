import os
import json

import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from jobportal.models import Exam, QuizQuestion


QUESTION_BANK_DIR = os.path.join(
    "jobportal",
    "question_banks"
)


def get_questions(data):

    # Format 1:
    # {
    #     "exam": "District Court",
    #     "questions": [...]
    # }

    if isinstance(data, dict):

        return (
            data.get("exam"),
            data.get("questions", [])
        )

    # Format 2:
    # [
    #     {
    #         "exam_name": "Telangana AEE",
    #         ...
    #     }
    # ]

    if isinstance(data, list):

        if not data:
            return None, []

        exam_name = None

        if isinstance(data[0], dict):
            exam_name = data[0].get(
                "exam_name"
            )

        return exam_name, data

    return None, []


def get_value(item, *names, default=""):

    for name in names:

        value = item.get(name)

        if value is not None:
            return str(value).strip()

    return default


def main():

    total_added = 0
    total_skipped = 0
    total_errors = 0

    for filename in sorted(
        os.listdir(QUESTION_BANK_DIR)
    ):

        if not filename.endswith(".json"):
            continue

        # Never import backup files
        if "backup" in filename.lower():
            continue

        filepath = os.path.join(
            QUESTION_BANK_DIR,
            filename
        )

        print()
        print("=" * 70)
        print("FILE:", filename)

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8-sig"
            ) as f:

                data = json.load(f)

        except Exception as e:

            print("ERROR READING JSON:", e)
            total_errors += 1
            continue

        exam_name, questions = get_questions(data)

        if not exam_name:

            print("SKIPPED: Exam name not found")
            total_errors += 1
            continue

        exam = Exam.objects.filter(
            name__iexact=exam_name.strip()
        ).first()

        if not exam:

            print(
                "SKIPPED: Exam not found in database:",
                exam_name
            )

            total_errors += 1
            continue

        print("EXAM:", exam.name)
        print("JSON QUESTIONS:", len(questions))

        added = 0
        skipped = 0

        for item in questions:

            if not isinstance(item, dict):
                skipped += 1
                continue

            question_text = get_value(
                item,
                "question",
                "Question"
            )

            if not question_text:
                skipped += 1
                continue

            # -----------------------------------------
            # Duplicate check
            # -----------------------------------------

            exists = QuizQuestion.objects.filter(
                exam=exam,
                question=question_text
            ).exists()

            if exists:
                skipped += 1
                continue

            # -----------------------------------------
            # Read options
            # -----------------------------------------

            option1 = get_value(
                item,
                "option1",
                "option_1",
                "Option1",
                "A",
                "a"
            )

            option2 = get_value(
                item,
                "option2",
                "option_2",
                "Option2",
                "B",
                "b"
            )

            option3 = get_value(
                item,
                "option3",
                "option_3",
                "Option3",
                "C",
                "c"
            )

            option4 = get_value(
                item,
                "option4",
                "option_4",
                "Option4",
                "D",
                "d"
            )

            answer = get_value(
                item,
                "answer",
                "correct_answer",
                "correct",
                "Answer"
            )

            subject = get_value(
                item,
                "subject",
                "Subject",
                default="General"
            )

            difficulty = get_value(
                item,
                "difficulty",
                "Difficulty",
                default="Medium"
            )

            source = get_value(
                item,
                "source",
                "Source",
                default=filename
            )

            # -----------------------------------------
            # Normalize difficulty
            # -----------------------------------------

            if difficulty not in [
                "Medium",
                "Tough"
            ]:

                difficulty = "Medium"

            # -----------------------------------------
            # Create question
            # -----------------------------------------

            try:

                QuizQuestion.objects.create(
                    exam=exam,
                    question=question_text,
                    option1=option1,
                    option2=option2,
                    option3=option3,
                    option4=option4,
                    answer=answer,
                    subject=subject[:100],
                    difficulty=difficulty,
                    source=source[:200]
                )

                added += 1

            except Exception as e:

                print(
                    "ERROR importing question:",
                    e
                )

                total_errors += 1

        print("ADDED:", added)
        print("SKIPPED/DUPLICATES:", skipped)

        total_added += added
        total_skipped += skipped

    print()
    print("=" * 70)
    print("IMPORT COMPLETE")
    print("=" * 70)
    print("TOTAL ADDED:", total_added)
    print("TOTAL SKIPPED:", total_skipped)
    print("TOTAL ERRORS:", total_errors)
    print("=" * 70)


if __name__ == "__main__":
    main()