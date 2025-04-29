from playwright.sync_api import sync_playwright
import time

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled", "--no-sandbox", "--disable-setuid-sandbox"])
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Fanduel NBA page...")
        page.goto("https://sportsbook.fanduel.com/navigation/nba")
        page.wait_for_load_state("networkidle")

        try:
            print("Waiting for Player Points tab to be visible...")
            player_points_tab = page.locator("text=Player Points").first
            player_points_tab.wait_for(state="visible", timeout=10000)
            print("Clicking Player Points tab...")
            player_points_tab.click()

            print("Waiting for props to load...")
            page.wait_for_selector("div[data-testid='selection-card']", timeout=10000)

            print("Scraping props...")
            props = page.query_selector_all("div[data-testid='selection-card']")
            for prop in props:
                try:
                    player_name = prop.query_selector("div[class*='event-cell__name']").inner_text()
                    prop_value = prop.query_selector("span[class*='outcome-price']").inner_text()
                    print(f"{player_name}: {prop_value}")
                except Exception as e:
                    print(f"Error extracting a prop: {e}")

        except Exception as e:
            print(f"Error scraping: {e}")

        finally:
            print("Closing browser...")
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
