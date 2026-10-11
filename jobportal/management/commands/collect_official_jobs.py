import re
import requests

from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from django.utils import timezone

from pypdf import PdfReader

from jobportal.models import Job


class Command(BaseCommand):

    help = "Collect verified government recruitment notifications"

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/154.0.0.0 Safari/537.36"
        )
    }

    OFFICIAL_SOURCES = {
        "UPSC": (
            "https://www.upsc.gov.in/"
            "recruitment/recruitment-advertisement"
        ),
        "Telangana Police Recruitment Board": (
            "https://www.tgprb.in/"
        ),
    }

    def add_arguments(self, parser):

        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Do not save jobs to database",
        )

    # ============================================================
    # MAIN
    # ============================================================

    def handle(self, *args, **options):

        dry_run = options["dry_run"]

        self.stdout.write("")
        self.stdout.write("=" * 70)
        self.stdout.write(
            "OFFICIAL GOVERNMENT JOB COLLECTOR"
        )
        self.stdout.write("=" * 70)

        if dry_run:

            self.stdout.write(
                self.style.WARNING(
                    "DRY RUN MODE - DATABASE WILL NOT BE CHANGED"
                )
            )

        self.stdout.write("")

        all_jobs = []

        # --------------------------------------------------------
        # UPSC
        # --------------------------------------------------------

        try:

            self.stdout.write(
                "Checking official source: UPSC"
            )

            upsc_jobs = self.collect_upsc_jobs()

            all_jobs.extend(
                upsc_jobs
            )

        except Exception as e:

            self.stdout.write(
                self.style.ERROR(
                    f"UPSC collector error: {e}"
                )
            )

        # --------------------------------------------------------
        # TGPRB
        # --------------------------------------------------------

        try:

            self.stdout.write(
                "Checking official source: "
                "Telangana Police Recruitment Board"
            )

            tgprb_jobs = (
                self.collect_tgprb_jobs()
            )

            all_jobs.extend(
                tgprb_jobs
            )

        except Exception as e:

            self.stdout.write(
                self.style.ERROR(
                    f"TGPRB collector error: {e}"
                )
            )

        # --------------------------------------------------------
        # REMOVE DUPLICATES
        # --------------------------------------------------------

        all_jobs = (
            self.remove_duplicates(
                all_jobs
            )
        )

        self.stdout.write("")
        self.stdout.write("=" * 70)

        self.stdout.write(
            f"TOTAL VERIFIED OFFICIAL NOTIFICATIONS: "
            f"{len(all_jobs)}"
        )

        self.stdout.write("=" * 70)
        self.stdout.write("")

        # --------------------------------------------------------
        # DRY RUN
        # --------------------------------------------------------

        if dry_run:

            self.stdout.write(
                self.style.SUCCESS(
                    "DRY RUN COMPLETE"
                )
            )

            self.stdout.write(
                "No database records were created or updated."
            )

            return

        # --------------------------------------------------------
        # SAVE
        # --------------------------------------------------------

        saved_count = 0

        for job_data in all_jobs:

            try:

                job, created = (
                    Job.objects.update_or_create(
                        official_link=job_data[
                            "official_link"
                        ],
                        defaults=job_data,
                    )
                )

                saved_count += 1

                if created:

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"CREATED: {job.title}"
                        )
                    )

                else:

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"UPDATED: {job.title}"
                        )
                    )

            except Exception as e:

                self.stdout.write(
                    self.style.ERROR(
                        f"Database error: {e}"
                    )
                )

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully saved/updated: "
                f"{saved_count}"
            )
        )

    # ============================================================
    # UPSC
    # ============================================================

    def collect_upsc_jobs(self):

        jobs = []

        url = self.OFFICIAL_SOURCES["UPSC"]

        try:

            response = requests.get(
                url,
                headers=self.HEADERS,
                timeout=30,
            )

            response.raise_for_status()

        except Exception as e:

            self.stdout.write(
                self.style.ERROR(
                    f"Unable to read UPSC page: {e}"
                )
            )

            return jobs

        html = response.text

        # --------------------------------------------------------
        # Find PDF links
        # --------------------------------------------------------

        pdf_links = re.findall(
            r'href=["\']([^"\']+\.pdf[^"\']*)["\']',
            html,
            re.IGNORECASE,
        )

        absolute_links = []

        for link in pdf_links:

            if link.startswith("/"):

                link = (
                    "https://www.upsc.gov.in"
                    + link
                )

            elif link.startswith("./"):

                link = (
                    "https://www.upsc.gov.in/"
                    + link[2:]
                )

            elif not link.startswith("http"):

                continue

            if "advt" in link.lower():

                absolute_links.append(
                    link
                )

        absolute_links = list(
            dict.fromkeys(
                absolute_links
            )
        )

        # --------------------------------------------------------
        # Only 2026 advertisements
        # --------------------------------------------------------

        current_links = [
            link
            for link in absolute_links
            if "2026" in link
        ]

        current_links.sort(
            reverse=True
        )

        # --------------------------------------------------------
        # Process each PDF
        # --------------------------------------------------------

        for pdf_url in current_links:

            try:

                self.stdout.write(
                    f"Reading official UPSC PDF: "
                    f"{pdf_url}"
                )

                text = (
                    self.download_pdf_text(
                        pdf_url
                    )
                )

                if not text:

                    continue

                advertisement_number = (
                    self.extract_upsc_advertisement_number(
                        pdf_url,
                        text,
                    )
                )

                if not advertisement_number:

                    continue

                last_date = (
                    self.extract_last_date(
                        text
                    )
                )

                if not last_date:

                    self.stdout.write(
                        self.style.WARNING(
                            "Skipped - last date not found"
                        )
                    )

                    continue

                notification_date = (
                    self.get_upsc_notification_date(
                        pdf_url
                    )
                )

                if not notification_date:

                    notification_date = (
                        timezone.now().date()
                    )

                vacancies = (
                    self.extract_vacancy_total(
                        text
                    )
                )

                title = (
                    "UPSC Advertisement No. "
                    f"{advertisement_number}/2026"
                )

                description = (
                    "Official recruitment notification "
                    "issued by the Union Public Service "
                    "Commission. Advertisement No. "
                    f"{advertisement_number}/2026. "
                    "Candidates should read the official "
                    "notification for complete eligibility, "
                    "vacancies, dates and application "
                    "instructions."
                )

                job_data = {
                    "title": title,
                    "organization": (
                        "Union Public Service Commission"
                    ),
                    "job_type": "Central",
                    "category": "UPSC",
                    "state": "All India",
                    "location": "All India",
                    "qualification": (
                        "As mentioned in official notification"
                    ),
                    "age_limit": (
                        "As mentioned in official notification"
                    ),
                    "vacancies": vacancies,
                    "salary": "As Per Rules",
                    "application_mode": "Online",
                    "notification_date": notification_date,
                    "last_date": last_date,
                    "official_link": pdf_url,
                    "description": description,
                    "is_latest": True,
                }

                jobs.append(
                    job_data
                )

                self.stdout.write("")

                self.stdout.write(
                    self.style.SUCCESS(
                        f"FOUND: {title}"
                    )
                )

                self.stdout.write(
                    f"Organization: "
                    f"{job_data['organization']}"
                )

                self.stdout.write(
                    f"Category: "
                    f"{job_data['category']}"
                )

                self.stdout.write(
                    f"Notification Date: "
                    f"{notification_date}"
                )

                self.stdout.write(
                    f"Vacancies: {vacancies}"
                )

                self.stdout.write(
                    f"Last Date: {last_date}"
                )

                self.stdout.write(
                    f"Official URL: {pdf_url}"
                )

                self.stdout.write(
                    "Government Type: Central"
                )

                self.stdout.write(
                    "State: All India"
                )

                self.stdout.write("")

            except Exception as e:

                self.stdout.write(
                    self.style.ERROR(
                        f"UPSC PDF processing error: {e}"
                    )
                )

        if not jobs:

            self.stdout.write(
                "No verified official UPSC "
                "recruitment notification found."
            )

        return jobs

    # ============================================================
    # UPSC ADVERTISEMENT NUMBER
    # ============================================================

    def extract_upsc_advertisement_number(
        self,
        pdf_url,
        text,
    ):

        match = re.search(
            r"AdvtNo-(\d+)-2026",
            pdf_url,
            re.IGNORECASE,
        )

        if match:

            return match.group(1)

        match = re.search(
            r"ADVT\.?\s*NO\.?\s*(\d+)\s*/\s*2026",
            text,
            re.IGNORECASE,
        )

        if match:

            return match.group(1)

        return None

    # ============================================================
    # UPSC NOTIFICATION DATE
    # ============================================================

    def get_upsc_notification_date(
        self,
        official_url,
    ):

        match = re.search(
            r"AdvtNo-\d+-2026-[A-Za-z]+-(\d{6})",
            official_url,
            re.IGNORECASE,
        )

        if not match:

            return None

        value = match.group(1)

        try:

            return datetime.strptime(
                value,
                "%d%m%y",
            ).date()

        except ValueError:

            return None

    # ============================================================
    # PDF DOWNLOAD
    # ============================================================

    def download_pdf_text(
        self,
        url,
    ):

        try:

            response = requests.get(
                url,
                headers=self.HEADERS,
                timeout=60,
            )

            response.raise_for_status()

            temp_dir = Path(
                "tmp_official_pdfs"
            )

            temp_dir.mkdir(
                exist_ok=True
            )

            filename = (
                url.split("/")[-1]
                .split("?")[0]
            )

            if not filename.lower().endswith(
                ".pdf"
            ):

                filename = "notification.pdf"

            pdf_path = (
                temp_dir / filename
            )

            pdf_path.write_bytes(
                response.content
            )

            reader = PdfReader(
                str(pdf_path)
            )

            pages = []
            seen_pages = set()

            for page in reader.pages:

                try:

                    page_text = (
                        page.extract_text()
                        or ""
                    ).strip()

                    if not page_text:
                        continue

                    normalized_page = re.sub(
                        r"\s+",
                        " ",
                        page_text
                    ).strip()

                    if normalized_page in seen_pages:
                        continue

                    seen_pages.add(
                        normalized_page
                    )

                    pages.append(
                        page_text
                    )

                except Exception:

                    continue

            return "\n".join(
                pages
            )

        except Exception as e:

            self.stdout.write(
                self.style.ERROR(
                    f"PDF error: {e}"
                )
            )

            return ""

    def extract_vacancy_total(self, text):

        if not text:
            return 0

        units = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
        }

        tens = {
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90,
        }

        def words_to_number(value):

            value = value.lower().replace("-", " ")
            words = value.split()

            total = 0
            current = 0

            for word in words:

                if word == "and":
                    continue

                if word in units:
                    current += units[word]

                elif word in tens:
                    current += tens[word]

                elif word == "hundred":
                    if current == 0:
                        current = 1

                    current *= 100

                elif word == "thousand":
                    if current == 0:
                        current = 1

                    total += current * 1000
                    current = 0

            return total + current

        word_list = (
            "one|two|three|four|five|six|seven|eight|nine|"
            "ten|eleven|twelve|thirteen|fourteen|fifteen|"
            "sixteen|seventeen|eighteen|nineteen|twenty|"
            "thirty|forty|fifty|sixty|seventy|eighty|ninety|"
            "hundred|thousand|and"
        )

        vacancy_pattern = re.compile(
            r"(?:\d+\.\s*)?"
            r"\(Vacancy\s+No\.\s*[^)]*\)"
            r"\s*"
            r"(.*?)(?="
            r"(?:\d+\.\s*)?"
            r"\(Vacancy\s+No\."
            r"|$)",
            re.IGNORECASE | re.DOTALL,
        )

        word_pattern = re.compile(
            rf"\b((?:{word_list})"
            rf"(?:[\s-]+(?:{word_list}))*)"
            r"\s+vacanc(?:y|ies)\b",
            re.IGNORECASE,
        )

        numeric_pattern = re.compile(
            r"\b(\d{1,6})\s+vacanc(?:y|ies)\b",
            re.IGNORECASE,
        )

        clean_text = re.sub(r"\s+", " ", text).strip()

        entries = vacancy_pattern.findall(clean_text)

        found = []

        for entry in entries:

            value = None

            word_match = word_pattern.search(entry)

            if word_match:
                value = words_to_number(
                    word_match.group(1)
                )

            if value is None:

                numeric_match = numeric_pattern.search(entry)

                if numeric_match:
                    value = int(
                        numeric_match.group(1)
                    )

            if value is not None and 0 < value <= 100000:
                found.append(value)

        total = sum(found)

        self.stdout.write(
            f"Detected vacancy entries: {found}"
        )

        self.stdout.write(
            f"Calculated vacancy total: {total}"
        )

        return total

    # ============================================================
    # LAST DATE
    # ============================================================

    def extract_last_date(
        self,
        text,
    ):

        if not text:

            return None

        patterns = [

            (
                r"closing\s+date.*?"
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})"
            ),

            (
                r"last\s+date.*?"
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})"
            ),

            (
                r"application.*?"
                r"closing.*?"
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})"
            ),

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL,
            )

            if match:

                date_value = (
                    self.parse_date(
                        match.group(1)
                    )
                )

                if date_value:

                    return date_value

        # --------------------------------------------------------
        # Written dates
        # --------------------------------------------------------

        written_pattern = re.compile(
            r"\b(\d{1,2})"
            r"(?:st|nd|rd|th)?\s+"
            r"(January|February|March|April|May|June|July|"
            r"August|September|October|November|December)"
            r"\s+(\d{4})",
            re.IGNORECASE,
        )

        for match in written_pattern.finditer(
            text
        ):

            try:

                return datetime.strptime(
                    (
                        f"{match.group(1)} "
                        f"{match.group(2)} "
                        f"{match.group(3)}"
                    ),
                    "%d %B %Y",
                ).date()

            except ValueError:

                continue

        return None

    # ============================================================
    # DATE PARSER
    # ============================================================

    def parse_date(
        self,
        value,
    ):

        formats = [
            "%d/%m/%Y",
            "%d-%m-%Y",
            "%d/%m/%y",
            "%d-%m-%y",
            "%m/%d/%Y",
            "%m-%d-%Y",
        ]

        for fmt in formats:

            try:

                return datetime.strptime(
                    value.strip(),
                    fmt,
                ).date()

            except ValueError:

                continue

        return None

    # ============================================================
    # TGPRB
    # ============================================================

    def collect_tgprb_jobs(
        self,
    ):

        jobs = []

        url = self.OFFICIAL_SOURCES[
            "Telangana Police Recruitment Board"
        ]

        try:

            response = requests.get(
                url,
                headers=self.HEADERS,
                timeout=30,
            )

            response.raise_for_status()

        except Exception as e:

            self.stdout.write(
                self.style.ERROR(
                    f"Unable to read TGPRB website: {e}"
                )
            )

            return jobs

        html = response.text

        pdf_links = re.findall(
            r'href=["\']([^"\']+\.pdf[^"\']*)["\']',
            html,
            re.IGNORECASE,
        )

        verified_links = []

        for link in pdf_links:

            if link.startswith("/"):

                link = (
                    "https://www.tgprb.in"
                    + link
                )

            elif link.startswith("./"):

                link = (
                    "https://www.tgprb.in/"
                    + link[2:]
                )

            lower = link.lower()

            if (
                "recruit" in lower
                or "notification" in lower
                or "notifi" in lower
                or "constable" in lower
                or "si" in lower
            ):

                verified_links.append(
                    link
                )

        verified_links = list(
            dict.fromkeys(
                verified_links
            )
        )

        for pdf_url in verified_links:

            try:

                text = (
                    self.download_pdf_text(
                        pdf_url
                    )
                )

                if not text:

                    continue

                lower_text = (
                    text.lower()
                )

                keywords = [
                    "recruitment",
                    "notification",
                    "vacancies",
                    "online application",
                ]

                match_count = sum(
                    1
                    for keyword in keywords
                    if keyword in lower_text
                )

                if match_count < 2:

                    continue

                last_date = (
                    self.extract_last_date(
                        text
                    )
                )

                if not last_date:

                    continue

                vacancies = (
                    self.extract_vacancy_total(
                        text
                    )
                )

                notification_date = (
                    self.extract_first_date(
                        text
                    )
                )

                if not notification_date:

                    notification_date = (
                        timezone.now().date()
                    )

                title = (
                    self.extract_tgprb_title(
                        text
                    )
                )

                if not title:

                    title = (
                        "Telangana Police "
                        "Recruitment Notification"
                    )

                job_data = {
                    "title": title,
                    "organization": (
                        "Telangana State Level "
                        "Police Recruitment Board"
                    ),
                    "job_type": "Telangana",
                    "category": "Police",
                    "state": "Telangana",
                    "location": "Telangana",
                    "qualification": (
                        "As mentioned in official notification"
                    ),
                    "age_limit": (
                        "As mentioned in official notification"
                    ),
                    "vacancies": vacancies,
                    "salary": "As Per Rules",
                    "application_mode": "Online",
                    "notification_date": notification_date,
                    "last_date": last_date,
                    "official_link": pdf_url,
                    "description": (
                        "Official Telangana Police "
                        "recruitment notification."
                    ),
                    "is_latest": True,
                }

                jobs.append(
                    job_data
                )

                self.stdout.write("")
                self.stdout.write(
                    self.style.SUCCESS(
                        f"FOUND: {title}"
                    )
                )
                self.stdout.write(
                    f"Vacancies: {vacancies}"
                )
                self.stdout.write(
                    f"Last Date: {last_date}"
                )
                self.stdout.write(
                    f"Official URL: {pdf_url}"
                )
                self.stdout.write("")

            except Exception as e:

                self.stdout.write(
                    self.style.ERROR(
                        f"TGPRB PDF error: {e}"
                    )
                )

        if not jobs:

            self.stdout.write(
                "No verified official recruitment notification found."
            )

        return jobs

    # ============================================================
    # TGPRB TITLE
    # ============================================================

    def extract_tgprb_title(
        self,
        text,
    ):

        if not text:

            return None

        match = re.search(
            r"(.{0,100}"
            r"(?:RECRUITMENT|NOTIFICATION)"
            r".{0,150})",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if not match:

            return None

        title = (
            match.group(0)
            .replace("\n", " ")
        )

        title = re.sub(
            r"\s+",
            " ",
            title,
        ).strip()

        return title[:200]

    # ============================================================
    # FIRST DATE FROM TEXT
    # ============================================================

    def extract_first_date(
        self,
        text,
    ):

        pattern = re.compile(
            r"\b(\d{1,2})[/-]"
            r"(\d{1,2})[/-]"
            r"(\d{4})\b"
        )

        dates = []

        for match in pattern.finditer(
            text
        ):

            try:

                value = datetime.strptime(
                    (
                        f"{match.group(1)}/"
                        f"{match.group(2)}/"
                        f"{match.group(3)}"
                    ),
                    "%d/%m/%Y",
                ).date()

                dates.append(
                    value
                )

            except ValueError:

                continue

        if dates:

            return min(
                dates
            )

        return None

    # ============================================================
    # REMOVE DUPLICATES
    # ============================================================

    def remove_duplicates(
        self,
        jobs,
    ):

        unique = {}

        for job in jobs:

            official_link = job.get(
                "official_link"
            )

            if not official_link:

                continue

            unique[
                official_link
            ] = job

        return list(
            unique.values()
        )
