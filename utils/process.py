# this function is used to process the data that we scrape from the seminar websites
# goal is to retrieve the future seminars with date and title announced
# approach: save a local version and then compare it with the newly scrapped data?

#region set up
import pandas as pd
import os

# we only need the difference between the scrapped and local data
def compare(df1, df2):
    # this function compares two dataframes and returns the differences
    # it uses the pandas merge function to find the differences
    # it returns a dataframe with the differences
    df = pd.merge(df1, df2, how='outer', indicator=True)
    df = df[df['_merge'] != 'both']
    df = df.drop(columns=['_merge'])
    
    return df

# evaluate the differences and keep the rows where we have complete info
def evaluate(df):
    # this function evaluates the differences and keeps the rows where we have complete info
    # it uses the pandas dropna function to drop the rows with missing values
    # it returns a dataframe with the complete rows
    df = df[['']]
    
    return df

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
