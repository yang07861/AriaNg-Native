from playwright.sync_api import sync_playwright, expect
import time
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Navigate to the index.html file
    page.goto(f"file://{os.getcwd()}/app/index.html")

    # Wait for the page to load
    expect(page.locator('aside.main-sidebar')).to_be_visible(timeout=10000)
    time.sleep(3)

    # Navigate to settings and enable auto-retry
    page.click('a[href="#!/settings/ariang"]')
    time.sleep(1)
    page.screenshot(path="jules-scratch/verification/settings-page.png")

    # Navigate back to main page and verify toolbar
    page.click('a[href="#!/downloading"]')
    time.sleep(1)

    # Take screenshot of the toolbar
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)