# main script
#DONE: allow reset for each semester
#DONE: clean the tables (allow for varying  format)
#TODO: add econ history (static), rockwool seminar (dynamic)


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

# semester path
semester_path = os.path.join(folder_path, sem)
print(f"Semester path: {semester_path}")

# if we are starting a new semester, we need to create a new folder
if isdir(semester_path):
    # set the new_sem parater, need it for later if statements
    new_sem = False
else:    
    new_sem = True
    
    # create a folder for the semester
    os.makedirs(semester_path, exist_ok=True)
    
    # enumerate through the seminar list and scrap each seminar
    for s in seminar_list:
        # scrap the seminar website
        df = scrap_google(s.url)
        
        # save the scraped data to a local file using the name provided
        file_path = os.path.join(semester_path, f"{s.name}.csv")
        print(file_path)
        df.to_csv(file_path, index=False)
        print(f"Saved {s.name} data to {s.path}")


# update the semester for each seminar object
for s in seminar_list:
    s.semester = sem
    s.path = os.path.join(semester_path, f"{s.name}.csv")  # update the path to the local file

#region main
def basic(s):
    '''
    s for class seminar
    this function calls the scrap_google function to scrape the seminar websites,
    compares the scraped data with the local data, and saves the new data to a local file,
    for newly added data, evaluate whether the information is complete,
    if we have complete information, send a calendar invite to myself (user)
    '''
    # get both new and old data
    #df_new = scrap_google(s.url)
    
    df = pd.read_csv(s.path)
    
    # compare the two
    #diff = compare(df_new, df_old)
    
    # shorten the data
    event_rows = simplify_data(s, df)
    
    # filter for rows for events later than the start date
    event_rows = event_rows[event_rows['Date'] >= start_date]

        
    # --- Create the calendar ---
    calendar = Calendar()
    for index, row in event_rows.iterrows():
       # print(f"Number of rows to process: {len(event_rows)}")
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
    
    return None

for index, s in enumerate(seminar_list):
    
        calendar = basic(s)
    