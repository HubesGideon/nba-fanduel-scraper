from playwright.sync_api import sync_playwright
import time

def scrape_fanduel_nba_points():
    print("Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
        )
        page = context.new_page()

        try:
            print("Navigating to Fanduel NBA page...")
            page.goto("https://sportsbook.fanduel.com/navigation/nba", timeout=60000)
            page.wait_for_load_state("networkidle")
            print("Successfully navigated to page.")
        except Exception as e:
            print(f"Error navigating to page: {e}")
            browser.close()
            return

        try:
            print("Waiting for Player Points tab to be visible...")
            player_points_tab = page.locator("text=Player Points").first
            player_points_tab.wait_for(state="visible", timeout=10000)
            print("Clicking Player Points tab...")
            player_points_tab.click()
        except Exception as e:
            print(f"Error clicking Player Points tab: {e}")
            browser.close()
            return

        try:
            print("Scraping props...")
            page.wait_for_selector("[data-testid='event-cell']", timeout=10000)
            events = page.query_selector_all("[data-testid='event-cell']")

            for event in events:
                player_name = event.query_selector("[data-testid='participant-name']").inner_text()
                prop_value = event.query_selector("[data-testid='bet-price']").inner_text()
                print(f"{player_name}: {prop_value}")

        except Exception as e:
            print(f"Error scraping props: {e}")

        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
