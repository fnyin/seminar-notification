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
import pytz
import subprocess


#region inputs
project_root = '/Users/fan/Dropbox/projects/programming/scrap-seminar'
sem = "2025SoSe" # set the semester to the current semester
start_date = datetime(2025, 4, 15) # set the start date to the earlist date you want to trace back the seminar invites. only matters for init
seminar_list = [BAMS, BQSE] # store seminare you want to get updates from!


#region set up
## paths
# Set the working directory to the project root (or any absolute path)
os.chdir(project_root)

# set time zone for the starting date
berlin = pytz.timezone('Europe/Berlin')
start_date = berlin.localize(datetime(2025, 5, 24))


# update the semester for each seminar object
for s in seminar_list:
    s.semester = sem

#region main
def basic(s, start):    
    df = scrap_google(s.url)

    # shorten the data
    event_rows = simplify_data(s, df)
    
    # filter for rows for events later than the start date
    event_rows = event_rows[event_rows['Date'] >= start]

    return event_rows

def create_cal(s_list, start):
    calendar = Calendar()
    for s in s_list:
        event_rows = basic(s, start)
        
        for index, row in event_rows.iterrows():
        # print(f"Number of rows to process: {len(event_rows)}")
            try:
                event = create_event(s, row)
                calendar.events.add(event)
                print(f"Added event: {event.name} on {event.begin}")
            except Exception as e:
                print(f"Error creating event for row {index}: {e}")
        
        
    ics_filename = f"berlin_econ_seminar_calendar.ics"
    with open(ics_filename, "w") as f:
        f.writelines(calendar)

    print(f"\n📅 ICS file saved as {ics_filename}")
    
    return None
    

create_cal(seminar_list, start_date)
