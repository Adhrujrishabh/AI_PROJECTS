import time
from playwright.sync_api import sync_playwright

print("🚀 Launching the Ultra-Stealth Enterprise Penetration Engine...")
with sync_playwright() as p:
    # launch a single background browser controller core
    browser = p.chromium.launch(headless=False)

    print("Spawning engine Alpha (Target quotes sandbox)...")
    page_alpha = browser.new_page()
    page_alpha.goto("https://quotes.toscrape.com/", wait_until="domcontentloaded")

    print("Spawning engine Beta (Target E-commerce store)...")
    page_beta = browser.new_page()
    page_beta.goto("https://scrapingcourse.com/", wait_until="domcontentloaded")

    print("syncronizing paraller engine wait states...")
    time.sleep(4)
    print("📸 Extracting multi-engine snapshot proofs...")
    page_alpha.screenshot(path="engine_alpha_proof.png")
    page_beta.screenshot(path="engine_beta_proof.png",)

    print("safely shutting down concurrent browser context stream...")
    browser.close()

print("🎉 SUCCESS: DUAL-Engine parallel run executed flawlessly!")