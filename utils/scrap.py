# plan: two functions, one for scrapping a dynamic website, another for when we have access to the google sheet
# this script scrapes information from the seminar websites and store them as ics files
# it uses playwright to handle dynamic content since all the seminar info is loaded via a google sheet that i don't have access to

# static google sheets
import requests
from bs4 import BeautifulSoup
import pandas as pd

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

def compare(df1, df2):
    # this function compares two dataframes and returns the differences
    # it uses the pandas merge function to find the differences
    # it returns a dataframe with the differences
    df = pd.merge(df1, df2, how='outer', indicator=True)
    df = df[df['_merge'] != 'both']
    df = df.drop(columns=['_merge'])
    
    return df

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
