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
            
            # Add your real logic here
            page.locator("text=Popular").first.wait_for(state="visible", timeout=10000)
            props = page.query_selector_all(".some-prop-class")  # <-- replace as needed
            
            for prop in props:
                print(prop.inner_text())
        
        except Exception as e:
            print(f"Error scraping: {e}")
        
        finally:
            browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
