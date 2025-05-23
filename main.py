# main script
#TODO: allow reset for each semester
#TODO: perplexity API to search for speaker and return short bio, website link, and paper link
#TODO: clean the tables (allow for varying format)


from utils.scrap import *
from utils.seminar_class import seminar
from utils.process import *
from utils.info import *
import os
from os.path import isdir
import pandas as pd
from ics import Calendar, Event

#region inputs
project_root = '/Users/fan/Dropbox/projects/programming/scrap-seminar'
sem = "2025SoSe" # set the semester to the current semester
start_date = datetime(2025, 5, 24) # set the start date to the earlist date you want to trace back the seminar invites. only matters for init
seminar_list = [BAMS, BQSE] # store seminare you want to get updates from!


#region set up
## paths
# Set the working directory to the project root (or any absolute path)
os.chdir(project_root)

# create the folder relative to this working directory
folder_path = "data"
os.makedirs(folder_path, exist_ok=True)

# if we are starting a new semester, we need to create a new folder
if isdir(folder_path):
    # set the new_sem parater, need it for later if statements
    new_sem = False
else:    
    new_sem = True
    
    # create a folder for the semester
    folder_path = os.path.join(folder_path, sem)
    os.makedirs(folder_path, exist_ok=True)
    
    # enumerate through the seminar list and scrap each seminar
    for s in seminar_list:
        # scrap the seminar website
        df = scrap_google(s.url)
        
        # save the scraped data to a local file using the name provided
        file_path = os.path.join(folder_path, f"{s.name}.csv")
        df.to_csv(file_path, index=False)
        print(f"Saved {s.name} data to {s.path}")

# update semester for each seminar
def set_sem(s, semester):
    '''
    this function updates the semester of the seminar object
    '''
    s.semester = semester
    
    return s

# update the semester for each seminar object
for s in seminar_list:
    s = set_sem(s, '2023 Fall')

#region main
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
    
    # shorten the data
    event_rows = simplify_data(s, diff)
    
    if new_sem:
        # if we are starting a new semester, the seminar list is likely to be very long, so we only keep until our desired date
        event_rows = event_rows[event_rows['Date'] >= start_date]
        
    # --- Create the calendar ---
    calendar = Calendar()
    for index, row in event_rows.iterrows():
        try:
            event = create_event(s, row)
            calendar.events.add(event)
            print(f"Added event: {event.name} on {event.begin}")
        except Exception as e:
            print(f"Error creating event for row {index}: {e}")
    
    # --- Save to ICS file ---
    ics_filename = f"{s.name.lower().replace(' ', '_')}_calendar.ics"
    with open(ics_filename, "w") as f:
        f.writelines(calendar)

    print(f"\n📅 ICS file saved as: {ics_filename}")
    
    return diff


