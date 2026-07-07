import csv
import time 
from playwright.sync_api import sync_playwright , TimeoutError

print("initializing the master mega robot extraction pipeline...")

human_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

Csv_file = open("master_leads_database.csv", mode="w", newline="", encoding="utf-8")
writer = csv.writer(Csv_file)
writer.writerow(["Scrapped text"]) # Write the column header row!

with sync_playwright() as p:
    # Launch a real, visible Google Chrome window
    browser = p.chromium.launch(headless=False)
    
    # Create the stealth context wrapper pre-loaded with our human identity mask!
    context = browser.new_context(user_agent=human_agent)
    page = context.new_page()
    
    print("🌐 Connecting directly to our data matrix in stealth mode...")
    page.goto("https://www.scrapingcourse.com/ecommerce/", wait_until="domcontentloaded")

    time.sleep(2)

    print("📊 Extracting targeted data metrics from the website...")
    
    # Locate all the text headlines on the page view grid
    page.locator("h2").first.wait_for()
    text_elements = page.locator("h2")
    headlines = text_elements.all_inner_texts()

    print(f"💰 Harvested {len(headlines)} fresh text rows successfully!")
    
    # Loop through our text list array and dump each item into the Excel file columns
    for item in headlines:
        writer.writerow([item])
        print(f"   ✍️ Recording row: {item[:30]}...")

    print("📸 Snapping master proof screenshot...")
    page.screenshot(path="master_pipeline_proof.png")
    
    print("🛑 Task complete. Closing master browser session cleanly...")
    browser.close()

# Close the file system connection line at the absolute left margin margin
print("🎉 SUCCESS: Master Mega-Robot loop complete. Excel database populated perfectly!")
