from playwright.sync_api import sync_playwright
import time

def scrape_fanduel_nba_points():
    print("Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"]
        )
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Fanduel NBA page...")
        try:
            page.goto("https://sportsbook.fanduel.com/navigation/nba")
            page.wait_for_load_state("networkidle")
            print("Successfully navigated to page.")
        except Exception as e:
            print(f"Error navigating to page: {e}")
            browser.close()
            return

        try:
            # Wait for "Player Points" tab
            page.locator('text=Player Points').first.wait_for(timeout=10000)
            page.locator('text=Player Points').first.click()
            print("Clicked on Player Points tab.")
        except Exception as e:
            print(f"Error clicking Player Points: {e}")
            browser.close()
            return

        try:
            # Example scraping: grabbing all player props under Player Points
            props = page.locator(".event-cell__name-text").all_text_contents()
            for prop in props:
                print(prop)
        except Exception as e:
            print(f"Error scraping props: {e}")

        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
