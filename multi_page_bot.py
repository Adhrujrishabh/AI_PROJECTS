import time
from playwright.sync_api import sync_playwright

print("🚀 Launching the Multi-Page Catalog Crawler Bot...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("🌐 Connecting directly to the bookstore directory catalog...")
    # This URL is completely updated to go directly into the books subsystem!
    page.goto("http://books.toscrape.com/index.html")
    time.sleep(2)
    
    for current_page in range(1, 4):
        print(f"📖 System Scan: Parsing catalog grid layout on Page {current_page}...")
        
        book_elements = page.locator("h3 a")
        titles = book_elements.all_inner_texts()
        
        print(f"   📊 Harvested item titles from page grid!")
        
        if current_page < 3:
            print("➡️ Target Found: Clicking the 'next' pagination button...")
            page.click("text=next")
            time.sleep(2)
            
    print("📸 Snapping visual proof of multi-page tracking loop...")
    page.screenshot(path="multi_page_success.png")
    
    print("🛑 Closing browser engine...")
    browser.close()

print("🎉 SUCCESS: Your automated robot looped page layouts perfectly!")
