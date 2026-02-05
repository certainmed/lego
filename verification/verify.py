
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        print(f"Loading {file_path}")
        page.goto(file_path)

        # Wait for control panel
        page.wait_for_selector("#control-panel")

        # Verify absence of removed buttons
        # Load, Camera, Help
        assert page.query_selector("#load-btn") is None, "Load button should be removed"
        assert page.query_selector("#reset-camera") is None, "Reset Camera button should be removed"
        assert page.query_selector("#help-btn") is None, "Help button should be removed"

        print("Removed buttons verified.")

        # Verify presence of new buttons
        # Clone, Grid, Theme, Select All
        clone_btn = page.query_selector("#clone-btn")
        grid_btn = page.query_selector("#grid-btn")
        theme_btn = page.query_selector("#theme-btn")
        select_all_btn = page.query_selector("#select-all-btn")

        assert clone_btn is not None, "Clone button missing"
        assert grid_btn is not None, "Grid button missing"
        assert theme_btn is not None, "Theme button missing"
        assert select_all_btn is not None, "Select All button missing"

        print("New buttons verified.")

        # Take a screenshot of the control panel area
        # Toggle theme to see difference
        theme_btn.click()
        page.wait_for_timeout(500) # Wait for potential transition

        # Take full screenshot
        page.screenshot(path="verification/verification.png")
        print("Screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
