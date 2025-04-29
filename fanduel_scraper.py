from playwright.sync_api import sync_playwright

def scrape_fanduel_nba_points():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to FanDuel NBA page
        page.goto("https://sportsbook.fanduel.com/navigation/nba")
        page.wait_for_timeout(10000)  # Wait for page to load
        
        # Expand the NBA player points section
        try:
            # This selector finds the 'Player Points' market tab and clicks it
            page.locator("text=Player Points").first.click()
            page.wait_for_timeout(5000)  # Wait for props to load
        except Exception as e:
            print(f"Could not find or click 'Player Points' section: {e}")
        
        # Now grab all player props
        player_props = []
        
        try:
            player_cards = page.query_selector_all("div.event-cell__name-text")  # player names
            odds_blocks = page.query_selector_all("div.market-outcome")  # odds info
            
            for i in range(min(len(player_cards), len(odds_blocks) // 2)):
                player_name = player_cards[i].inner_text()
                
                # Each player has two outcomes: Over and Under
                over_block = odds_blocks[2 * i]
                under_block = odds_blocks[2 * i + 1]
                
                over_text = over_block.inner_text().split("\n")
                under_text = under_block.inner_text().split("\n")
                
                try:
                    line = float(over_text[0])  # e.g., 26.5 points
                except:
                    line = None  # if parsing fails
                
                try:
                    over_odds = int(over_text[1].replace("−", "-"))  # Handle minus signs
                except:
                    over_odds = None
                
                try:
                    under_odds = int(under_text[1].replace("−", "-"))
                except:
                    under_odds = None
                
                player_props.append({
                    "player_name": player_name,
                    "line": line,
                    "over_odds": over_odds,
                    "under_odds": under_odds
                })
        
        except Exception as e:
            print(f"Error scraping props: {e}")
        
        # Print out the results
        for prop in player_props:
            print(prop)
        
        browser.close()

if __name__ == "__main__":
    scrape_fanduel_nba_points()
