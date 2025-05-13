# this script scrapes information from the seminar websites and store them as ics files
from playwright.sync_api import sync_playwright

def scrape_seminar_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to the seminar site
        page.goto("https://sites.google.com/site/berlinappliedmicroseminar/", timeout=60000)
        
        # Wait for dynamic content to load
        page.wait_for_timeout(10000)  # 10 seconds

        # Extract text from the main content div
        content = page.locator("div#sites-canvas-main-content").inner_text()

        browser.close()
        return content

if __name__ == "__main__":
    seminar_info = scrape_seminar_text()
    print(seminar_info)
