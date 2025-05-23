# need to import the seminar class from seminar.py
from utils.seminar_class import seminar
from ics import Calendar, Event
from datetime import datetime, timedelta, time

#region url
# collect url and locator from all websites
# manually update url and locator if the website changes/add new website
# hopefully this is the only thing that needs to be updated
BAMS_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRshH4QuzsOR3f9RtwAaC8yfk-WYiSynZ4FXMdy07UJcl1mRxDIAc26r8Pafydld1dQqNENo7rc93v0/pubhtml?gid=1189407793"


BQSE_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3J_S9rJVlljcVhC1IcG1IY-TkSl75PQAu8jZX9nnfZMx3Jceddn2wOa5WfE-hP5jpbwU_YbpY40Dx/pubhtml?gid=572234617"


# each seminar has a url, name, path, scrapper, location, time, and semester, as defined in the seminar class
BAMS = seminar(
    url = BAMS_url,
    name = 'BAMS',
    scraper= 'google',
    location  = 'Mohrenstraße 58, Ostrom room', # location just a string
    begin = time(hour=14, minute=0), # time is a datetime.time object
    duration = timedelta(hours=1.5)
)

BQSE = seminar(
    url = BQSE_url,
    name = 'BQSE',
    scraper= 'google',
    location  = 'Spandauer 1, Room 23', # location just a string
    begin = time(hour=16, minute=15),
    duration = timedelta(hours=1.5)
)

# Econ history:
# table element: everything under #parent-fieldname-text > div > table

# rockwool
