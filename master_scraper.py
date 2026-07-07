import csv
import time
from itertools import zip_longest
from playwright.sync_api import sync_playwright

print("Initializing product scraper...")

human_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

with open("master_leads_database.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Product Name", "Price", "Availability"])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=human_agent)
        page = context.new_page()

        print("Opening website...")
        page.goto(
            "https://www.scrapingcourse.com/ecommerce/",
            wait_until="domcontentloaded"
        )

        time.sleep(2)

        titles = page.locator("h2").all_inner_texts()
        prices = page.locator("span.price").all_inner_texts()
        stock_statuses = page.locator(".stock").all_inner_texts()

        print("Titles:", len(titles))
        print("Prices:", len(prices))
        print("Stock:", len(stock_statuses))

        for title, price, stock in zip_longest(
            titles,
            prices,
            stock_statuses,
            fillvalue="Not found"
        ):
            writer.writerow([title, price, stock])
            print(f"Saved: {title[:30]} | {price} | {stock}")

        page.screenshot(path="master_pipeline_proof.png", full_page=True)
        browser.close()

print("SUCCESS: CSV database populated.")