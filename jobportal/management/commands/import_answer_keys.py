import json
from pathlib import Path

from django.core.management.base import BaseCommand

from jobportal.models import AnswerKey


class Command(BaseCommand):
    help = "Import verified historical government exam answer keys."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            default="govtjobs_verified_answer_keys.json",
            help="Path to the verified answer keys JSON file.",
        )

        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate the JSON without saving records to the database.",
        )

    def handle(self, *args, **options):

        file_path = Path(options["file"])
        dry_run = options["dry_run"]

        # ---------------------------------------------------------
        # Check JSON file
        # ---------------------------------------------------------

        if not file_path.exists():

            self.stdout.write(
                self.style.ERROR(
                    f"File not found: {file_path}"
                )
            )

            return

        self.stdout.write(
            self.style.SUCCESS(
                f"Reading answer-key file: {file_path}"
            )
        )

        # ---------------------------------------------------------
        # Load JSON
        # ---------------------------------------------------------

        try:

            with file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

        except json.JSONDecodeError as exc:

            self.stdout.write(
                self.style.ERROR(
                    f"Invalid JSON file: {exc}"
                )
            )

            return

        except OSError as exc:

            self.stdout.write(
                self.style.ERROR(
                    f"Unable to read file: {exc}"
                )
            )

            return

        # ---------------------------------------------------------
        # JSON must contain a list
        # ---------------------------------------------------------

        if not isinstance(data, list):

            self.stdout.write(
                self.style.ERROR(
                    "JSON root must be a list of answer-key records."
                )
            )

            return

        # ---------------------------------------------------------
        # Counters
        # ---------------------------------------------------------

        created = 0
        updated = 0
        skipped = 0
        invalid = 0

        # ---------------------------------------------------------
        # Verified statuses
        # ---------------------------------------------------------

        verified_statuses = {
            "confirmed_official_answer_key_notice",
            "confirmed_official_answer_key_archive",
            "confirmed_official_final_answer_key_notice",
            "confirmed_official_tentative_answer_key",
            "confirmed_official_answer_key_release",
            "confirmed_official_key_page",
            "confirmed_official",
        }

        # ---------------------------------------------------------
        # Process records
        # ---------------------------------------------------------

        for index, record in enumerate(data, start=1):

            # -----------------------------------------------------
            # Record must be a dictionary
            # -----------------------------------------------------

            if not isinstance(record, dict):

                invalid += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"[{index}] Skipped: record is not an object."
                    )
                )

                continue

            # -----------------------------------------------------
            # Read basic fields
            # -----------------------------------------------------

            exam_name = (
                record.get("exam_name")
                or record.get("exam")
                or ""
            )

            exam_name = str(exam_name).strip()

            title = (
                record.get("title")
                or ""
            )

            title = str(title).strip()

            year = record.get("year")

            status = (
                record.get("status")
                or ""
            )

            status = str(status).strip()

            answer_key_url = (
                record.get("answer_key_url")
                or ""
            )

            answer_key_url = str(answer_key_url).strip()

            official_source_url = (
                record.get("official_source_url")
                or record.get("official_link")
                or ""
            )

            official_source_url = str(
                official_source_url
            ).strip()

            shift = (
                record.get("shift")
                or ""
            )

            shift = str(shift).strip()

            set_name = (
                record.get("set_name")
                or ""
            )

            set_name = str(set_name).strip()

            paper_code = (
                record.get("paper_code")
                or ""
            )

            paper_code = str(paper_code).strip()

            notes = (
                record.get("notes")
                or ""
            )

            notes = str(notes).strip()

            category = (
                record.get("category")
                or "Other"
            )

            category = str(category).strip()

            # -----------------------------------------------------
            # Exam name required
            # -----------------------------------------------------

            if not exam_name:

                invalid += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"[{index}] Skipped: exam name missing."
                    )
                )

                continue

            # -----------------------------------------------------
            # Validate examination year
            # -----------------------------------------------------

            try:

                if year is None or str(year).strip() == "":

                    invalid += 1

                    self.stdout.write(
                        self.style.WARNING(
                            f"[{index}] Skipped: examination year "
                            f"missing for {exam_name}"
                        )
                    )

                    continue

                year = int(year)

            except (ValueError, TypeError):

                invalid += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"[{index}] Skipped: invalid examination year "
                        f"for {exam_name}: {year}"
                    )
                )

                continue

            # -----------------------------------------------------
            # Historical period required by GovtJobs
            # 2015 through 2026
            # -----------------------------------------------------

            if year < 2015 or year > 2026:

                invalid += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"[{index}] Skipped: year outside supported "
                        f"period (2015-2026): "
                        f"{exam_name} {year}"
                    )
                )

                continue

            # -----------------------------------------------------
            # ONLY genuine verified answer keys
            # -----------------------------------------------------

            is_verified = (
                status in verified_statuses
                and bool(answer_key_url)
            )

            if not is_verified:

                skipped += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"[{index}] Skipped unverified record: "
                        f"{exam_name} {year}"
                    )
                )

                continue

            # -----------------------------------------------------
            # Optional question / answer data
            # -----------------------------------------------------

            question_data = record.get(
                "question_data",
                None
            )

            answer_data = record.get(
                "answer_data",
                None
            )

            # -----------------------------------------------------
            # Convert dictionaries/lists to JSON strings
            # if the model fields are TextField/JSON-compatible
            # -----------------------------------------------------

            if isinstance(question_data, (dict, list)):

                question_data = json.dumps(
                    question_data,
                    ensure_ascii=False
                )

            if isinstance(answer_data, (dict, list)):

                answer_data = json.dumps(
                    answer_data,
                    ensure_ascii=False
                )

            # -----------------------------------------------------
            # Display information
            # -----------------------------------------------------

            self.stdout.write(
                f"[{index}] "
                f"{exam_name} | "
                f"{year} | "
                f"{status}"
            )

            if dry_run:

                self.stdout.write(
                    self.style.SUCCESS(
                        "    VALID - dry run"
                    )
                )

                continue

            # -----------------------------------------------------
            # Build defaults
            # -----------------------------------------------------

            defaults = {
                "title": title,
                "category": category,
                "official_link": official_source_url,
                "answer_key_url": answer_key_url,
                "status": status,
                "notes": notes,
                "shift": shift,
                "set_name": set_name,
                "paper_code": paper_code,
            }

            # -----------------------------------------------------
            # Add optional data only when supplied
            # -----------------------------------------------------

            if question_data is not None:
                defaults["question_data"] = question_data

            if answer_data is not None:
                defaults["answer_data"] = answer_data

            # -----------------------------------------------------
            # Find existing record
            #
            # One exam can have multiple shifts / sets / papers
            # in the same year.
            # -----------------------------------------------------

            lookup = {
                "exam_name": exam_name,
                "year": year,
                "shift": shift,
                "set_name": set_name,
                "paper_code": paper_code,
            }

            # -----------------------------------------------------
            # Update or create
            # -----------------------------------------------------

            try:

                obj, created_flag = (
                    AnswerKey.objects.update_or_create(
                        **lookup,
                        defaults=defaults
                    )
                )

            except Exception as exc:

                invalid += 1

                self.stdout.write(
                    self.style.ERROR(
                        f"    Database error for "
                        f"{exam_name} {year}: {exc}"
                    )
                )

                continue

            # -----------------------------------------------------
            # Counters
            # -----------------------------------------------------

            if created_flag:

                created += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"    CREATED: "
                        f"{exam_name} {year}"
                    )
                )

            else:

                updated += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"    UPDATED: "
                        f"{exam_name} {year}"
                    )
                )

        # ---------------------------------------------------------
        # Final report
        # ---------------------------------------------------------

        self.stdout.write("")
        self.stdout.write("=" * 60)
        self.stdout.write("ANSWER KEY IMPORT SUMMARY")
        self.stdout.write("=" * 60)

        self.stdout.write(
            f"Total JSON records : {len(data)}"
        )

        self.stdout.write(
            f"Created            : {created}"
        )

        self.stdout.write(
            f"Updated            : {updated}"
        )

        self.stdout.write(
            f"Skipped            : {skipped}"
        )

        self.stdout.write(
            f"Invalid            : {invalid}"
        )

        self.stdout.write(
            "Supported years    : 2015 - 2026"
        )

        self.stdout.write(
            "Verified URLs only : YES"
        )

        self.stdout.write("=" * 60)

        # ---------------------------------------------------------
        # Dry-run message
        # ---------------------------------------------------------

        if dry_run:

            self.stdout.write(
                self.style.WARNING(
                    "DRY RUN: No database records were changed."
                )
            )

        else:

            self.stdout.write(
                self.style.SUCCESS(
                    "Answer-key import completed."
                )
            )