import time
from playwright.sync_api import sync_playwright

print("🚀 Launching the automated browser bot engine...")

with sync_playwright() as p:
    # headless=False means we want to VISUALLY see the browser open and move on our screen!
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("🌐 Navigating the robot directly to the mock bookstore site...")
    page.goto("http://toscrape.com")
    
    # Wait for 3 seconds so we can visually look at the page
    time.sleep(3)
    
    print("📸 Taking a live automated snapshot of the site grid layout...")
    page.screenshot(path="automation_screenshot.png")
    
    print("🛑 Closing the browser system down...")
    browser.close()

print("🎉 SUCCESS: Your robot completed its first automation patrol run!")
