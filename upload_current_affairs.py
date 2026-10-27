
import getpass
import json
import os
from pathlib import Path

import requests

BASE_URL = "https://govtjobs-x6jz.onrender.com"
JSON_FILE = Path("current_affairs_export.json")

if not JSON_FILE.is_file():
    raise SystemExit(f"File not found: {JSON_FILE.resolve()}")

token = getpass.getpass("Render import token: ")
username = input("Django staff username: ")
password = getpass.getpass("Django staff password: ")

session = requests.Session()

# Open the Django admin login page.
login_page = session.get(
    f"{BASE_URL}/admin/login/",
    timeout=60,
)
login_page.raise_for_status()

# Log in using the staff account.
from html.parser import HTMLParser


class CSRFParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.token = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "input" and attrs.get("name") == "csrfmiddlewaretoken":
            self.token = attrs.get("value")


parser = CSRFParser()
parser.feed(login_page.text)

csrf = parser.token or session.cookies.get("csrftoken")

if not csrf:
    raise SystemExit("Could not find the Django login CSRF token.")

login_response = session.post(
    f"{BASE_URL}/admin/login/",
    data={
        "username": username,
        "password": password,
        "csrfmiddlewaretoken": csrf,
        "next": "/admin/",
    },
    headers={"Referer": f"{BASE_URL}/admin/login/"},
    timeout=60,
)

login_response.raise_for_status()

if "/admin/login/" in login_response.url:
    raise SystemExit(
        "Login was not successful. Check your staff credentials."
    )

# Read and validate the local export before uploading.
with JSON_FILE.open("r", encoding="utf-8") as file:
    records = json.load(file)

if not isinstance(records, list) or len(records) != 228:
    raise SystemExit(
        f"Expected 228 records; found "
        f"{len(records) if isinstance(records, list) else 'invalid JSON'}."
    )


# Upload the records to the protected Render endpoint.

batch_size = 10
total_created = 0
total_skipped = 0

for start in range(0, len(records), batch_size):
    batch = records[start:start + batch_size]

    print(
        f"Uploading records {start + 1}-"
        f"{start + len(batch)} of {len(records)}..."
    )

    response = session.post(
        f"{BASE_URL}/temporary-current-affairs-import/",
        json=batch,
        headers={
            "X-Import-Token": token,
            "Referer": f"{BASE_URL}/admin/",
        },
        timeout=120,
    )

    print("HTTP status:", response.status_code)
    print("Server response:", response.text[:1000])
    response.raise_for_status()

    result = response.json()
    total_created += result.get("created", 0)
    total_skipped += result.get("skipped", 0)

print("\nImport completed!")
print("Total records:", len(records))
print("Created:", total_created)
print("Skipped:", total_skipped)


print("HTTP status:", response.status_code)
print("Response content type:", response.headers.get("Content-Type"))
print("Response body:", response.text[:3000])

response.raise_for_status()

