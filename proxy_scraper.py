import time
from playwright.sync_api import sync_playwright

import os

USERNAME = os.getenv("WEBSHARE_USERNAME")
PASSWORD = os.getenv("WEBSHARE_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("Missing WEBSHARE_USERNAME or WEBSHARE_PASSWORD")

PROXY_POOL = [
    {"server": "http://31.59.20.176:6754", "username": USERNAME, "password": PASSWORD},
    {"server": "http://31.56.127.193:7684", "username": USERNAME, "password": PASSWORD},
    {"server": "http://45.38.107.97:6014", "username": USERNAME, "password": PASSWORD},
    {"server": "http://198.105.121.200:6462", "username": USERNAME, "password": PASSWORD},
    {"server": "http://64.137.96.74:6641", "username": USERNAME, "password": PASSWORD},
]

with sync_playwright() as p:
    for proxy in PROXY_POOL:
        browser = None

        try:
            print(f"Testing proxy: {proxy['server']}")

            browser = p.chromium.launch(
                headless=False,
                proxy=proxy
            )

            page = browser.new_page()
            page.goto("https://httpbin.org/ip", wait_until="domcontentloaded", timeout=30000)

            time.sleep(3)
            page.screenshot(path="proxy_routing_proof.png")

            print(f"SUCCESS: {proxy['server']} works")
            browser.close()
            break

        except Exception as e:
            print(f"FAILED: {proxy['server']}")
            print(e)

            if browser:
                browser.close()