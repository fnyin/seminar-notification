# this function is used to process the data that we scrape from the seminar websites
# goal is to retrieve the future seminars with date and title announced
# approach: save a local version and then compare it with the newly scrapped data?

import pandas as pd
import os
from utils.seminar_class import seminar
from ics import Calendar, Event
from datetime import datetime, timedelta, time
import pytz

#region data
# we only need the difference between the scrapped and local data
def compare(df1, df2):
    # haven't used this function, now 
    # this function compares two dataframes and returns the differences
    # it uses the pandas merge function to find the differences
    # it returns a dataframe with the differences
    df = pd.merge(df1, df2, how='outer', on=['Date',  'Speaker', 'Institution', 'Title'], indicator=True)
    # filter out rows that are present in both dataframes
    df = df[df['_merge'] != 'both']
    # drop the _merge column as it is not needed anymore
    df = df.drop(columns=['_merge'])
    
    return df

# simplify the data formt, keeping only what we need to create event
def simplify_data(s, df):
    # keep relevant columns
    if 'Place' not in df.columns:
        df['Place'] = s.location
    df = df[['Date', 'Place', 'Speaker', 'Institution', 'Title']]
    
    
    # formate date
    if s.name == 'BAMS':
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y', errors='coerce')

    else:
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y', errors='coerce')

    df['Date'] = df['Date'].dt.tz_localize('Europe/Berlin')
    
    # filter for rows with complete information
    complete = df.dropna(subset=['Date', 'Place', 'Speaker', 'Institution']) # allow missing titls for now
    # if there is no title, we can set it to 'TBC' or 'No seminar'
    complete['Title'] = complete['Title'].fillna('TBC')  # fill missing titles with TBC
    #complete = complete[complete['Title'] !=  'TBC']
    complete = complete[complete['Title'] !=  'No seminar'] # specific for bqse
    
    print(f"Number of complete rows for {s.name}: {len(complete)}")
    return complete

#region event
def create_event(s, row):
    event = Event()
    berlin = pytz.timezone('Europe/Berlin')
    
    # Title
    event.name = f"{s.name} - {row['Title']}"

    # Combine date from row and time from seminar object
    date_val = row['Date'].date() 
    time_val = s.begin             # Should be datetime.time
    
    naive_dt = datetime.combine(date_val, time_val)
    event.begin = berlin.localize(naive_dt)
    

    # Duration, location, etc.
    event.duration = s.duration
    event.location = s.location
    
    # update the location is not 'DIW'
    ## only applicable for applied micro
    if event.location == 'DIW':
        event.location = s.location
    else:
        event.location = row['Place']
        
    event.description = f"Speaker: {row['Speaker']}\nInstitution: {row['Institution']}"
    event.url = s.url

    return event
