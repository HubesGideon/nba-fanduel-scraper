from playwright.sync_api import sync_playwright
import time

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=False)  # Set to False so you can *see* what's happening
        page = browser.new_page()

        print("Navigating to Fanduel NBA page...")
        try:
            page.goto("https://sportsbook.fanduel.com/navigation/nba", timeout=60000)
            page.wait_for_load_state("networkidle")

            print("Successfully navigated to page.")

            # Now wait for the "Player Points" tab
            player_points_tab = page.locator("text=Player Points").first
            player_points_tab.wait_for(state="visible", timeout=10000)
            player_points_tab.click()

            print("Clicked Player Points tab.")

            # Wait for player props to appear
            time.sleep(5)  # Adjust if needed based on network speed

            props = page.query_selector_all('div[data-testid="selection-price"]')
            for prop in props:
                print(prop.inner_text())

        except Exception as e:
            print(f"Error scraping: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
