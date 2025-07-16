import os
import requests
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load API config from .env
load_dotenv()
API_BASE_URL = os.getenv("CANVAS_API_URL") + "/api/v1"
API_TOKEN = os.getenv("CANVAS_API_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

OUTPUT_DIR = "extracted_pages"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def list_pages(course_id):
    """Get all pages in the course"""
    pages = []
    url = f"{API_BASE_URL}/courses/{course_id}/pages"
    params = {"per_page": 100}
    while url:
        res = requests.get(url, headers=HEADERS, params=params)
        res.raise_for_status()
        pages.extend(res.json())
        url = res.links.get("next", {}).get("url")
    return pages


def fetch_page(course_id, page_url):
    """Get full HTML for a page"""
    url = f"{API_BASE_URL}/courses/{course_id}/pages/{page_url}"
    res = requests.get(url, headers=HEADERS)
    res.raise_for_status()
    return res.json()


def extract_text_with_links(html):
    """Convert HTML to readable text, preserving links"""
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            text = a.get_text(strip=True)
            a.string = f"{text} ({href})"
    return soup.get_text(separator="\n", strip=True)


def save_page_json(course_id, page_data):
    """Save page as .json with cleaned text"""
    title = page_data["title"]
    url = page_data["url"]
    html = page_data["body"]
    text = extract_text_with_links(html)

    output = {
        "title": title,
        "url": url,
        "canvas_course_id": course_id,
        "text": text
    }

    filename = f"{course_id}_{url}.json".replace("/", "_")
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✔ Saved: {filename}")


def main():
    course_id = input("Enter Canvas course ID: ").strip()
    try:
        course_id = int(course_id)
    except ValueError:
        print("❌ Invalid course ID.")
        return

    print("🔍 Fetching page list...")
    pages = list_pages(course_id)
    print(f"📄 Found {len(pages)} pages.")

    for page in pages:
        full_data = fetch_page(course_id, page["url"])
        save_page_json(course_id, full_data)


if __name__ == "__main__":
    main()
