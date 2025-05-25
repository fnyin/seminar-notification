# define a class called seminar
# import packages needed for the class
from ics import Calendar, Event
from datetime import datetime, timedelta, time


class seminar:
    '''
    this class is used to process the data that we scrape from the seminar websites
    goal is to retrieve the future seminars with date and title announced
    approach: save a local version and then compare it with the newly scrapped data?
    '''
    
    def __init__(self, url, name, scraper, location, duration, semester = None,  path = None, begin = None):
        """
        self.url = url
        self.name = name
        self.path = path
        self.scraper = scraper
        self.location = location
        self.time_slot = time_slotname of the seminar.
        path (str): The local path to save seminar data.
        scraper (object): The scraper object used to fetch seminar data.
        loc (str): The location of the seminar.
        time (str): The time of the seminar.
        semester (str): The semester of the seminar, this will be updated every time user resets the semester
        """
        self.url = url
        self.name = name
        self.location = location
        self.duration = duration
        self.semester = semester
        self.path = path
        self.scraper = scraper
        self.begin = begin