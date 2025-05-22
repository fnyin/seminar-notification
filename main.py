# main script
#TODO: allow reset for each semester
#TODO: perplexity API to search for speaker and return short bio, website link, and paper link
#TODO: clean the tables (allow for varying format)


#region set up
from utils.scrap import *
from utils.seminar_class import seminar
import os
import pandas as pd

#region inputs
project_root = '/Users/fan/Dropbox/projects/programming/scrap-seminar'




# Set the working directory to the project root (or any absolute path)
os.chdir(project_root)

# create the folder relative to this working directory
folder_path = "data"
os.makedirs(folder_path, exist_ok=True)


#region url
# collect url and locator from all websites
# manually update url and locator if the website changes/add new website
BAMS_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRshH4QuzsOR3f9RtwAaC8yfk-WYiSynZ4FXMdy07UJcl1mRxDIAc26r8Pafydld1dQqNENo7rc93v0/pubhtml?gid=1189407793"
BAMS = scrap_google(BAMS_url)

print(BAMS.head())
print(BAMS.columns)

BQSE_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3J_S9rJVlljcVhC1IcG1IY-TkSl75PQAu8jZX9nnfZMx3Jceddn2wOa5WfE-hP5jpbwU_YbpY40Dx/pubhtml?gid=572234617"
BQSE = scrap_google(BQSE_url)
print(BQSE.head())
print(BQSE.columns)

# Econ history:
# table element: everything under #parent-fieldname-text > div > table

# rockwool


#region main function
def main(s):
    '''
    s for class seminar
    this function calls the scrap_google function to scrape the seminar websites,
    compares the scraped data with the local data, and saves the new data to a local file,
    for newly added data, evaluate whether the information is complete,
    if we have complete information, send a calendar invite to myself (user)
    '''
    # get both new and old data
    df_new = scrap_google(s.url)
    
    df_old = pd.read_csv(s.path)
    
    # compare the two
    diff = compare(df_new, df_old)
    
    
    
    # if the new data differs from the local data, save the new data to a local file
    # save the scraped data to a local file using the name provided
    file_path = os.path.join(folder_path, f"{s.name}.csv")
    df_new.to_csv(file_path, index=False)
    print(f"Saved {s.name} data to {s.path}")

    
    return None