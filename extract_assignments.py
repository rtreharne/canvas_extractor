import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_BASE_URL = os.getenv("CANVAS_API_URL") + "/api/v1"
API_TOKEN = os.getenv("CANVAS_API_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

OUTPUT_DIR = "extracted_assignments"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def list_assignments(course_id):
    assignments = []
    url = f"{API_BASE_URL}/courses/{course_id}/assignments"
    params = {"per_page": 100}
    while url:
        res = requests.get(url, headers=HEADERS, params=params)
        res.raise_for_status()
        assignments.extend(res.json())
        url = res.links.get("next", {}).get("url")
    return assignments

def save_assignments(course_id, assignments):
    for assignment in assignments:
        assignment_id = assignment["id"]
        filename = f"{course_id}_assignment_{assignment_id}.json"
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(assignment, f, indent=2)

        print(f"✔ Saved: {filename}")

def main():
    course_id = input("Enter Canvas course ID: ").strip()
    try:
        course_id = int(course_id)
    except ValueError:
        print("❌ Invalid course ID.")
        return

    print("🔍 Fetching assignments...")
    assignments = list_assignments(course_id)
    print(f"📝 Found {len(assignments)} assignments.")

    save_assignments(course_id, assignments)

if __name__ == "__main__":
    main()
