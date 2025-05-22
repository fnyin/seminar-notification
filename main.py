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
new_sem = False # only call set to True once before the semester starts
sem = '2024SoSe' # set the semester to the current semester
seminar_list = [] # store seminare objects you want to get updates from!

# Set the working directory to the project root (or any absolute path)
os.chdir(project_root)

# create the folder relative to this working directory
folder_path = "data"
os.makedirs(folder_path, exist_ok=True)

# update semester
def update_semester(s, semester):
    '''
    this function updates the semester of the seminar object
    '''
    s.semester = semester
    
    return s

if new_sem:
    # update the semester for each seminar object
    for s in seminar_list:
        s = update_semester(s, '2023 Fall')
        print(f"Updated {s.name} semester to {s.semester}")

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
    # file_path = os.path.join(folder_path, f"{s.name}.csv")
    # df_new.to_csv(file_path, index=False)
    # print(f"Saved {s.name} data to {s.path}")

    
    return diff



# initialize
# when using this tool for the first time, run this function first
def init(s):
    scrap_google(s.url)
    
    # save the scraped data to a local file using the name provided
    file_path = os.path.join(folder_path, f"{s.name}.csv")
    s.df.to_csv(file_path, index=False)
    print(f"Saved {s.name} data to {s.path}")
    
    return s.df