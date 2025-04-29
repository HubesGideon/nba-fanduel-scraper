from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Go to FanDuel NBA player points page (URL will be updated later)
        page.goto("https://sportsbook.fanduel.com/navigation/nba")
        page.wait_for_timeout(10000)  # Let page load 10 seconds
        
        # Placeholder — we'll add real scraping later
        print("Successfully loaded FanDuel NBA page!")
        
        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
