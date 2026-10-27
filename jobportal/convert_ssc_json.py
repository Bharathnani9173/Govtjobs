import json
import csv

json_file = "jobportal/ssc_cgl_questions.json"
csv_file = "jobportal/data/mock_questions_ssc_cgl.csv"

with open(json_file, "r", encoding="utf-8") as f:
    questions = json.load(f)

fields = [
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
]

with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for q in questions:
        writer.writerow({
            "exam_name": "SSC CGL",
            "subject": q["subject"],
            "question": q["question"],
            "option1": q["option1"],
            "option2": q["option2"],
            "option3": q["option3"],
            "option4": q["option4"],
            "answer": q["answer"],
            "explanation": "",
            "difficulty": q["difficulty"],
            "source": q["source"],
        })

print(f"Created CSV with {len(questions)} questions")