from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-software-rasterizer",
                "--disable-extensions",
                "--disable-setuid-sandbox",
                "--disable-infobars",
                "--remote-debugging-port=9222"
            ]
        )
        page = browser.new_page()

        try:
            print("Navigating to Fanduel NBA page...")
            page.goto("https://sportsbook.fanduel.com/navigation/nba", timeout=60000)
            page.wait_for_load_state("networkidle")

            print("Looking for 'Player Points' tab...")
            player_points_tab = page.locator("text=Player Points").first

            if player_points_tab.is_visible(timeout=10000):
                print("Found Player Points tab, clicking...")
                player_points_tab.click()
                page.wait_for_load_state("networkidle")

                # Example scraping after click (you'll adjust this later)
                props = page.query_selector_all(".your-prop-class")
                for prop in props:
                    print(prop.inner_text())

            else:
                print("Player Points tab not found.")

        except Exception as e:
            print(f"Error scraping: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
