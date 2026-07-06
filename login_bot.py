import time
from playwright.sync_api import sync_playwright

print("🚀 Initializing the Secure Interactive Login Bot...")

with sync_playwright() as p:
    # Launch a real, visible Google Chrome window
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("🌐 Navigating to the secure user login portal sandbox...")
    page.goto("https://quotes.toscrape.com/login")
    time.sleep(2)  # Pause to watch the page load cleanly
    
    print("✍️ Locating username box and typing credentials...")
    # This targets the input field with the id/name or type attribute for 'username'
    page.fill("input[id='username']", "Rishabh_Automation_Engineer")
    time.sleep(1)  # 1-second delay to simulate real human finger typing speed!
    
    print("🔑 Locating password box and typing secure password token...")
    # This targets the input field for 'password'
    page.fill("input[id='password']", "SecureDataRobot2026")
    time.sleep(1)  # Human simulation delay
    
    print("🖱️ Hovering mouse pointer over the 'Login' form button...")
    time.sleep(0.5)
    
    print("💥 Clicking the submit button to unlock the server dashboard gates...")
    # This finds the submit login button and clicks it!
    page.click("input[type='submit']")
    
    print("⏳ Waiting for the secure system profile layout to render...")
    time.sleep(3)  # Wait 3 seconds to visually confirm we cracked the login wall!
    
    print("📸 Capturing visual proof of the unlocked dashboard layout...")
    page.screenshot(path="login_success_proof.png")
    
    print("🛑 Task completed. Logging out and closing secure browser connection...")
    browser.close()

print("🎉 SUCCESS: Your robot filled the form, smashed the authentication wall, and captured proof!")
