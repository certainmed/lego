from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local file
        page.goto(f"file:///app/index.html")

        # Wait for title
        page.wait_for_selector("h1")

        # Check for Cheats section
        cheats_visible = page.is_visible("text=Cheats")
        print(f"Cheats section visible: {cheats_visible}")

        if not cheats_visible:
            print("Cheats section NOT found!")

        # Click No Clip
        page.click("#cheat-noclip")

        # Place a brick (canvas click)
        # Center of screen
        canvas = page.locator("#canvas-container")
        # We need to wait for canvas to be ready (three.js init)
        page.wait_for_timeout(1000)

        canvas.click(position={"x": 400, "y": 300})

        # Open Save Modal
        page.click("#save-btn")
        page.wait_for_selector("#save-modal.show")

        # Take screenshot
        page.screenshot(path="verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()
