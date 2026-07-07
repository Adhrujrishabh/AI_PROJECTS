import time
from playwright.sync_api import sync_playwright, TimeoutError

human_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(user_agent=human_agent)
    page = context.new_page()

    print("Opening website...")

    try:
        page.goto(
            "https://www.zoominfo.com",
            wait_until="domcontentloaded",
            timeout=60000
        )
    except TimeoutError:
        print("Page took too long, but keeping browser open...")

    time.sleep(10)
    page.screenshot(path="stealth_bot_success.png", full_page=True)

    input("Press Enter to close browser...")
    browser.close()