from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    print("Navigating to Fanduel NBA page...")
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
                "--remote-debugging-port=9222",
                "--single-process",
                "--disable-background-networking",
                "--disable-background-timer-throttling",
                "--disable-client-side-phishing-detection",
                "--disable-default-apps",
                "--disable-hang-monitor",
                "--disable-popup-blocking",
                "--disable-prompt-on-repost",
                "--metrics-recording-only",
                "--no-first-run",
                "--safebrowsing-disable-auto-update"
            ]
        )
        context = browser.new_context()
        page = context.new_page()
        
        try:
            page.goto("https://sportsbook.fanduel.com/navigation/nba", timeout=60000)
            print("Successfully navigated to page.")
            
            # Example locator usage, can be updated depending on what is needed
            page.wait_for_selector("text=Player Points", timeout=10000)
            print("Player Points tab found.")
            
            props = page.query_selector_all("selector-for-props")  # <-- Replace with correct selector
            print(f"Found {len(props)} props.")
            
            for prop in props:
                print(prop.inner_text())

        except Exception as e:
            print(f"Error scraping: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
