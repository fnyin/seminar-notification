# this function is used to process the data that we scrape from the seminar websites
# goal is to retrieve the future seminars with date and title announced
# approach: save a local version and then compare it with the newly scrapped data?

#region set up
import pandas as pd
import os


#region cleaning
def clean_data(df):
    '''
    this function cleans the data that we scrape from the seminar websites
    goal is to retrieve the future seminars with date and title announced
    approach: save a local version and then compare it with the newly scrapped data?
    '''
    # remove empty rows
    df = df.dropna(how='all')
    
    # remove empty columns
    df = df.dropna(axis=1, how='all')
    
    # remove duplicates
    df = df.drop_duplicates()
    
    # reset index
    df = df.reset_index(drop=True)
    
    return df
