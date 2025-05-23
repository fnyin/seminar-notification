# this function is used to process the data that we scrape from the seminar websites
# goal is to retrieve the future seminars with date and title announced
# approach: save a local version and then compare it with the newly scrapped data?

import pandas as pd
import os
from utils.seminar_class import seminar
from ics import Calendar, Event
from datetime import datetime, timedelta, time

#region data
# we only need the difference between the scrapped and local data
def compare(df1, df2):
    # this function compares two dataframes and returns the differences
    # it uses the pandas merge function to find the differences
    # it returns a dataframe with the differences
    df = pd.merge(df1, df2, how='outer', indicator=True)
    df = df[df['_merge'] != 'both']
    df = df.drop(columns=['_merge'])
    
    return df

# simplify the data formt, keeping only what we need to create event
def simplify_data(s, diff):
    # keep relevant columns
    if 'Place' not in diff.columns:
        diff['Place'] = s.location
    df = df[['Date', 'Place', 'Speaker', 'Institution', 'Title']]
    
    # filter for rows with complete information
    complete = df.dropna(subset=['Date', 'Place', 'Speaker', 'Institution', 'Title'])
    
    # formate date
    complete['Date'] = pd.to_datetime(complete['Date'], format='%d.%m.%Y')
    
    return df

#region event
def create_event(s, row):
    event = Event()
    
    # Title
    event.name = f"{s.name} - {row['Title']}"

    # Combine date from row and time from seminar object
    date_val = row['Date'].date() 
    time_val = s.begin             # Should be datetime.time
    event.begin = datetime.combine(date_val, time_val)

    # Duration, location, etc.
    event.duration = s.duration
    event.location = s.location
    event.description = f"Speaker: {row['Speaker']}\nInstitution: {row['Institution']}"
    event.url = s.url

    return event
