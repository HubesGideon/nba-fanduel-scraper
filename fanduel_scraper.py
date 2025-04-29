from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page()

        try:
            page.goto("https://sportsbook.fanduel.com/navigation/nba")
            page.wait_for_load_state("networkidle")  # wait until network is idle

            player_points_tab = page.locator("text=Player Points").first  # <-- fixed
            if player_points_tab.is_visible(timeout=10000):
                print("Player Points tab is visible!")
                player_points_tab.click()
                
                page.wait_for_load_state("networkidle")  # optional, wait after clicking

                # Now scrape whatever you need (example selector, change it for your props)
                props = page.query_selector_all(".your-prop-class")  # <-- you will need real CSS class here
                for prop in props:
                    print(prop.inner_text())
            else:
                print("Player Points tab not found after loading.")

        except Exception as e:
            print(f"Error scraping: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
