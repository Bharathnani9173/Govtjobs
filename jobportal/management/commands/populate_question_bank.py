import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from jobportal.models import Exam, QuizQuestion


class Command(BaseCommand):

    help = "Import exam question banks from JSON files"

    QUESTION_BANK_DIR = Path("jobportal/question_banks")
    TARGET_QUESTIONS = 200

    # JSON filename -> Django Exam name
    EXAM_FILES = {
        "ssc_cgl.json": "SSC CGL",
        "ssc_chsl.json": "SSC CHSL",
        "ssc_gd.json": "SSC GD",

        "rrb_group_d.json": "RRB Group D",
        "rrb_ntpc.json": "RRB NTPC",
        "rrb_alp.json": "RRB ALP",
        "rrb_technician.json": "RRB Technician",
        "rrb_je.json": "RRB JE",
        "railway_constable.json": "Railway Constable",
        "railway_si.json": "Railway SI",

        "ibps_po.json": "IBPS PO",
        "ibps_clerk.json": "IBPS Clerk",
        "sbi_po.json": "SBI PO",
        "sbi_clerk.json": "SBI Clerk",
        "banking.json": "Banking",

        "upsc_cse.json": "UPSC CSE",
        "upsc.json": "UPSC",

        "air_force.json": "Air Force",
        "army.json": "Army",

        "tet.json": "TET",

        "tspsc_group_1.json": "TSPSC Group 1",
        "tspsc_group_2.json": "TSPSC Group 2",
        "tspsc_group_3.json": "TSPSC Group 3",
        "tspsc_group_4.json": "TSPSC Group 4",

        "tgpsc_group_1.json": "TGPSC Group 1",
        "tgpsc_group_2.json": "TGPSC Group 2",
        "tgpsc_group_3.json": "TGPSC Group 3",
        "tgpsc_group_4.json": "TGPSC Group 4",

        "forest_range_officer.json": "Forest Range Officer",
        "telangana_ae.json": "Telangana AE",
        "telangana_aee.json": "Telangana AEE",

        "telangana_police_constable.json": "Telangana Police Constable",
        "telangana_police_si.json": "Telangana Police SI",

        "dsc.json": "DSC",

        "high_court.json": "High Court",
        "district_court.json": "District Court",

        "health_department.json": "Health Department",
        "revenue_department.json": "Revenue Department",
    }

    def normalize(self, value):
        if value is None:
            return ""

        return " ".join(str(value).strip().split())

    def question_key(self, question):
        """
        Used to detect duplicate questions.
        Comparison is case-insensitive and ignores extra spaces.
        """
        return self.normalize(question).lower()

    def handle(self, *args, **options):

        self.stdout.write("")
        self.stdout.write("=" * 70)
        self.stdout.write("      GOVTJOBS QUESTION BANK IMPORT")
        self.stdout.write("=" * 70)
        self.stdout.write("")

        if not self.QUESTION_BANK_DIR.exists():
            self.stdout.write(
                self.style.ERROR(
                    f"Question-bank directory not found: "
                    f"{self.QUESTION_BANK_DIR}"
                )
            )
            return

        total_added = 0
        total_duplicates = 0

        for filename, exam_name in self.EXAM_FILES.items():

            json_path = self.QUESTION_BANK_DIR / filename

            # -------------------------------------------------
            # JSON FILE DOES NOT EXIST
            # -------------------------------------------------
            if not json_path.exists():

                self.stdout.write(
                    self.style.WARNING(
                        f"{exam_name}: JSON file not found -> {filename}"
                    )
                )

                continue

            # -------------------------------------------------
            # FIND EXAM
            # -------------------------------------------------
            try:
                exam = Exam.objects.get(name=exam_name)

            except Exam.DoesNotExist:

                self.stdout.write(
                    self.style.ERROR(
                        f"{exam_name}: Exam does not exist in database."
                    )
                )

                continue

            # -------------------------------------------------
            # READ JSON
            # -------------------------------------------------
            try:

                with open(
                    json_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    data = json.load(file)

            except Exception as error:

                self.stdout.write(
                    self.style.ERROR(
                        f"{exam_name}: Could not read JSON -> {error}"
                    )
                )

                continue

            # -------------------------------------------------
            # VALIDATE JSON STRUCTURE
            # -------------------------------------------------
            if not isinstance(data, dict):

                self.stdout.write(
                    self.style.ERROR(
                        f"{exam_name}: JSON root must be an object."
                    )
                )

                continue

            json_questions = data.get("questions", [])

            if not isinstance(json_questions, list):

                self.stdout.write(
                    self.style.ERROR(
                        f"{exam_name}: 'questions' must be a list."
                    )
                )

                continue

            current_count = QuizQuestion.objects.filter(
                exam=exam
            ).count()

            self.stdout.write(
                f"EXAM: {exam_name}"
            )

            self.stdout.write(
                f"JSON QUESTIONS: {len(json_questions)}"
            )

            self.stdout.write(
                f"DATABASE QUESTIONS BEFORE: {current_count}"
            )

            # -------------------------------------------------
            # ALREADY 200
            # -------------------------------------------------
            if current_count >= self.TARGET_QUESTIONS:

                self.stdout.write(
                    self.style.SUCCESS(
                        f"ALREADY COMPLETE: "
                        f"{current_count}/{self.TARGET_QUESTIONS}"
                    )
                )

                self.stdout.write("")
                continue

            # -------------------------------------------------
            # EXISTING QUESTION KEYS
            # -------------------------------------------------
            existing_questions = QuizQuestion.objects.filter(
                exam=exam
            ).values_list(
                "question",
                flat=True
            )

            existing_keys = {
                self.question_key(question)
                for question in existing_questions
            }

            added = 0
            duplicates = 0

            # -------------------------------------------------
            # IMPORT QUESTIONS
            # -------------------------------------------------
            with transaction.atomic():

                for item in json_questions:

                    # Stop at exactly 200
                    if (
                        current_count + added
                        >= self.TARGET_QUESTIONS
                    ):
                        break

                    if not isinstance(item, dict):
                        continue

                    question = self.normalize(
                        item.get("question")
                    )

                    option1 = self.normalize(
                        item.get("option1")
                    )

                    option2 = self.normalize(
                        item.get("option2")
                    )

                    option3 = self.normalize(
                        item.get("option3")
                    )

                    option4 = self.normalize(
                        item.get("option4")
                    )

                    answer = self.normalize(
                        item.get("answer")
                    )

                    subject = self.normalize(
                        item.get(
                            "subject",
                            "General Knowledge"
                        )
                    )

                    difficulty = self.normalize(
                        item.get(
                            "difficulty",
                            "Medium"
                        )
                    )

                    source = self.normalize(
                        item.get(
                            "source",
                            "Practice"
                        )
                    )

                    # -------------------------------------------------
                    # REQUIRED FIELD CHECK
                    # -------------------------------------------------
                    if not all([
                        question,
                        option1,
                        option2,
                        option3,
                        option4,
                        answer,
                    ]):
                        self.stdout.write(
                            self.style.WARNING(
                                f"SKIPPED INVALID QUESTION: "
                                f"{question[:80]}"
                            )
                        )
                        continue

                    # -------------------------------------------------
                    # DUPLICATE CHECK
                    # -------------------------------------------------
                    key = self.question_key(question)

                    if key in existing_keys:

                        duplicates += 1
                        total_duplicates += 1

                        continue

                    # -------------------------------------------------
                    # CREATE QUESTION
                    # -------------------------------------------------
                    QuizQuestion.objects.create(
                        exam=exam,
                        question=question,
                        option1=option1,
                        option2=option2,
                        option3=option3,
                        option4=option4,
                        answer=answer,
                        subject=subject,
                        difficulty=difficulty,
                        source=source,
                    )

                    existing_keys.add(key)

                    added += 1
                    total_added += 1

            # -------------------------------------------------
            # FINAL COUNT
            # -------------------------------------------------
            final_count = QuizQuestion.objects.filter(
                exam=exam
            ).count()

            remaining = max(
                0,
                self.TARGET_QUESTIONS - final_count
            )

            self.stdout.write(
                f"ADDED: {added}"
            )

            self.stdout.write(
                f"DUPLICATES SKIPPED: {duplicates}"
            )

            self.stdout.write(
                f"TOTAL NOW: "
                f"{final_count}/{self.TARGET_QUESTIONS}"
            )

            if remaining > 0:

                self.stdout.write(
                    self.style.WARNING(
                        f"WARNING: {exam_name} still needs "
                        f"{remaining} questions."
                    )
                )

            else:

                self.stdout.write(
                    self.style.SUCCESS(
                        f"✓ {exam_name} COMPLETE: 200/200"
                    )
                )

            self.stdout.write("")

        # -----------------------------------------------------
        # FINAL SUMMARY
        # -----------------------------------------------------

        self.stdout.write("=" * 70)
        self.stdout.write("IMPORT COMPLETED")
        self.stdout.write("=" * 70)

        self.stdout.write(
            f"TOTAL QUESTIONS ADDED: {total_added}"
        )

        self.stdout.write(
            f"DUPLICATES SKIPPED: {total_duplicates}"
        )

        self.stdout.write("")
        self.stdout.write("QUESTION COUNTS:")
        self.stdout.write("")

        for filename, exam_name in self.EXAM_FILES.items():

            try:
                exam = Exam.objects.get(name=exam_name)

                count = QuizQuestion.objects.filter(
                    exam=exam
                ).count()

                self.stdout.write(
                    f"{exam_name}: "
                    f"{count}/{self.TARGET_QUESTIONS}"
                )

            except Exam.DoesNotExist:
                pass

        self.stdout.write("")
        self.stdout.write("=" * 70)

