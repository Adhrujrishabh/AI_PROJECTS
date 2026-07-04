import time
from playwright.sync_api import sync_playwright

print("🚀 Launching the Infinite Scroll Automation Engine...")

with sync_playwright() as p:
    # Launch a real, visible Google Chrome browser window
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("🌐 Navigating to a dynamic infinite scroll playground...")
    page.goto("https://toscrape.com")
    time.sleep(2)  # Pause to let the initial layout load smoothly
    
    # Let's simulate a human scrolling down 3 times to load hidden data!
    for i in range(1, 4):
        print(f"👇 Human Action: Scrolling down the page (Pass {i}/3)...")
        # This executes a JavaScript command to scroll to the absolute bottom of the window
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Wait 2 seconds for the server to load the brand-new elements onto the screen
        time.sleep(2)
    
    print("📸 Snapping visual proof of the fully expanded layout...")
    page.screenshot(path="infinite_scroll_proof.png")
    
    print("🛑 Task completed successfully. Shutting down browser...")
    browser.close()

print("🎉 SUCCESS: Your robot scrolled, loaded hidden layout text, and grabbed the data proof!")
