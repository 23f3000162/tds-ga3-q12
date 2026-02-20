from playwright.sync_api import sync_playwright
import re

URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=15",
    "https://sanand0.github.io/tdsdata/js_table/?seed=16",
    "https://sanand0.github.io/tdsdata/js_table/?seed=17",
    "https://sanand0.github.io/tdsdata/js_table/?seed=18",
    "https://sanand0.github.io/tdsdata/js_table/?seed=19",
    "https://sanand0.github.io/tdsdata/js_table/?seed=20",
    "https://sanand0.github.io/tdsdata/js_table/?seed=21",
    "https://sanand0.github.io/tdsdata/js_table/?seed=22",
    "https://sanand0.github.io/tdsdata/js_table/?seed=23",
    "https://sanand0.github.io/tdsdata/js_table/?seed=24",
]

def extract_numbers(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]

def main():
    total = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in URLS:
            page.goto(url)
            page.wait_for_selector("table")

            cells = page.query_selector_all("table td")

            for cell in cells:
                nums = extract_numbers(cell.inner_text())
                for n in nums:
                    total += n

        browser.close()

    print("FINAL TOTAL:", total)

if __name__ == "__main__":
    main()
