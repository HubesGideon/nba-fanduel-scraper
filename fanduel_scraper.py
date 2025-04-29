from playwright.sync_api import sync_playwright


def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page()

        try:
            print("Navigating to Fanduel NBA page...")
            page.goto("https://sportsbook.fanduel.com/navigation/nba")
            page.wait_for_load_state("networkidle")
            print("Successfully navigated to page.")

            # Example of finding the "Player Points" tab
            try:
                player_points_tab = page.locator("text=Player Points").first
                player_points_tab.wait_for(state="visible", timeout=10000)
                print("Found 'Player Points' tab.")

                # Click it if needed:
                player_points_tab.click()

                # You can now proceed with scraping props or whatever you want.

            except Exception as e:
                print(f"Error finding 'Player Points' tab: {e}")

        except Exception as e:
            print(f"Error navigating to page: {e}")

        finally:
            browser.close()


if __name__ == "__main__":
    scrape_fanduel_nba_points()
