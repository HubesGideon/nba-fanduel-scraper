import playwright.sync_api as p

def scrape_fanduel_nba_points():
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )
    page = browser.new_page()
    
    try:
        page.goto("https://sportsbook.fanduel.com/navigation/nba")
        
        # Add your logic here: waiting, clicking, scraping, etc
        # Example: wait for "Popular" section
        page.locator("text=Popular").first.wait_for(state="visible", timeout=10000)
        
        # Example scrape logic (adjust as needed)
        props = page.query_selector_all(".some-prop-class")  # <-- replace with your actual scraping target
        
        for prop in props:
            print(prop.inner_text())
    
    except Exception as e:
        print(f"Error scraping: {e}")
    
    finally:
        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
