from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to FanDuel NBA page
        page.goto("https://sportsbook.fanduel.com/navigation/nba")
        page.wait_for_timeout(12000)  # wait 12 seconds for full load
        
        try:
            # Click on 'Popular' tab if necessary (sometimes props are under it)
            popular_tab = page.locator("text=Popular").first
            if popular_tab.is_visible():
                popular_tab.click()
                page.wait_for_timeout(5000)
            
            # Click on "Player Points" market
            player_points_tab = page.locator("text=Player Points").first
            if player_points_tab.is_visible():
                player_points_tab.click()
                page.wait_for_timeout(5000)
            else:
                print("Player Points tab not found.")
        except Exception as e:
            print(f"Error navigating to Player Points: {e}")
        
        # Now scrape player props
        player_props = []
        
        try:
            player_cards = page.query_selector_all("div.event-cell__name-text")
            odds_blocks = page.query_selector_all("div.market-outcome")
            
            for i in range(min(len(player_cards), len(odds_blocks) // 2)):
                player_name = player_cards[i].inner_text()
                over_block = odds_blocks[2 * i]
                under_block = odds_blocks[2 * i + 1]
                
                over_text = over_block.inner_text().split("\n")
                under_text = under_block.inner_text().split("\n")
                
                line = float(over_text[0]) if over_text else None
                over_odds = int(over_text[1].replace("−", "-")) if len(over_text) > 1 else None
                under_odds = int(under_text[1].replace("−", "-")) if len(under_text) > 1 else None
                
                player_props.append({
                    "player_name": player_name,
                    "line": line,
                    "over_odds": over_odds,
                    "under_odds": under_odds
                })
        
        except Exception as e:
            print(f"Error scraping props: {e}")
        
        # Print out the scraped player props
        for prop in player_props:
            print(prop)
        
        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
