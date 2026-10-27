import os
import json

QUESTION_BANK_DIR = os.path.join(
    "jobportal",
    "question_banks"
)

for filename in sorted(os.listdir(QUESTION_BANK_DIR)):

    if not filename.endswith(".json"):
        continue

    if "backup" in filename.lower():
        continue

    filepath = os.path.join(
        QUESTION_BANK_DIR,
        filename
    )

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8-sig"
        ) as f:
            data = json.load(f)

        exam_name = None
        questions = []

        if isinstance(data, dict):

            exam_name = data.get("exam")

            questions = data.get(
                "questions",
                []
            )

        elif isinstance(data, list):

            questions = data

            if questions and isinstance(
                questions[0],
                dict
            ):
                exam_name = questions[0].get(
                    "exam_name"
                )

        print(
            f"{filename:35} | "
            f"{str(exam_name):30} | "
            f"{len(questions)} questions"
        )

    except Exception as e:

        print(
            f"{filename:35} | ERROR: {e}"
        )