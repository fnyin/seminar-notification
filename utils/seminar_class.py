# define a class called seminar
# import packages needed for the class

from utils.scrap import scrap_google
import pandas as pd

class seminar:
    '''
    this class is used to process the data that we scrape from the seminar websites
    goal is to retrieve the future seminars with date and title announced
    approach: save a local version and then compare it with the newly scrapped data?
    '''
    
    def __init__(self, url, name, path, scrapper, loc, time):
        self.url = url
        self.name = name
        self.path = path
        self.scrapper = scrapper
        self.location = loc
        self.time = time