# plan: two functions, one for scrapping a dynamic website, another for when we have access to the google sheet
# this script scrapes information from the seminar websites and store them as ics files
# it uses playwright to handle dynamic content since all the seminar info is loaded via a google sheet that i don't have access to

# static google sheets
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrap_google(url):
    # this function scrapes the google sheet and returns a pandas dataframe
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    print("Scraping Google Sheets...")

    # Grab all rows in the table
    table = soup.find("table")
    rows = table.find_all("tr")

    data = []
    for row in rows:
        cols = row.find_all(["th", "td"])
        data.append([cell.text.strip() for cell in cols])

    # Convert to DataFrame

    df = pd.DataFrame(data[1:], columns=data[1])

    return df

def econ_hist(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all table rows
    rows = soup.find_all('tr')

    seminar_data = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            date = cells[0].get_text(strip=True)
            details = cells[1].get_text(separator="\n", strip=True)

            # Split lines inside the details cell
            lines = [line.strip() for line in details.split("\n") if line.strip()]
            if len(lines) >= 2:
                speaker_info = lines[0]
                title = lines[1]
            else:
                speaker_info = lines[0]
                title = ""

            # Extract speaker and institution (using regex)
            match = re.match(r"(.+?)\s*\((.+?)\)", speaker_info)
            if match:
                speaker = match.group(1).strip()
                institution = match.group(2).strip()
            else:
                speaker = speaker_info.strip()
                institution = ""

            # Hardcode place (or scrape if available)
            place = "Berlin"

            seminar_data.append({
                'Date': date,
                #'Place': place,
                'Speaker': speaker,
                'Institution': institution,
                'Title': title
            })

    # Convert to DataFrame
    df = pd.DataFrame(seminar_data)

    # Reorder columns
    df = df[['Date',  'Speaker', 'Institution', 'Title']]
    
    return df

# Show DataFrame
#TODO: allow selection of column rows

# # WIP: dynamic
# from playwright.sync_api import sync_playwright

# def scrape_seminar_text(url, elem):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
        
#         # Go to the seminar site
#         page.goto(url, timeout=60000)
        
#         # Wait for dynamic content to load
#         page.wait_for_timeout(10000)  # 10 seconds, BQSE website needs this long

#         # Extract text from the main content div
#         content = page.locator(elem).inner_text()


#         browser.close()
#         return content

# if __name__ == "__main__":
#     seminar_info = scrape_seminar_text()
#     print(seminar_info)
