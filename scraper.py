import json
import time
from playwright.sync_api import sync_playwright

HASHTAG = "funny"
MAX_SCROLLS = 5

def scrape():
    videos = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.tiktok.com/tag/{HASHTAG}")

        time.sleep(5)

        for _ in range(MAX_SCROLLS):
            cards = page.query_selector_all("a[href*='/video/']")
            for card in cards:
                url = card.get_attribute("href")
                if url and url not in [v["url"] for v in videos]:
                    videos.append({
                        "url": f"https://www.tiktok.com{url}",
                        "used": False
                    })

            page.mouse.wheel(0, 3000)
            time.sleep(3)

        browser.close()

    with open("output/data.json", "w") as f:
        json.dump(videos, f, indent=2)

    print(f"✅ Trovati {len(videos)} video")

if __name__ == "__main__":
    scrape()

