# need to import the seminar class from seminar.py
from utils.seminar_class import seminar

#region url
# collect url and locator from all websites
# manually update url and locator if the website changes/add new website
# hopefully this is the only thing that needs to be updated
BAMS_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRshH4QuzsOR3f9RtwAaC8yfk-WYiSynZ4FXMdy07UJcl1mRxDIAc26r8Pafydld1dQqNENo7rc93v0/pubhtml?gid=1189407793"


BQSE_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3J_S9rJVlljcVhC1IcG1IY-TkSl75PQAu8jZX9nnfZMx3Jceddn2wOa5WfE-hP5jpbwU_YbpY40Dx/pubhtml?gid=572234617"


# each seminar has a url, name, path, scrapper, location, and time, as defined in the seminar class
BAMS = seminar(
    url = BAMS_url,
    name = 'BAMS',
    path = 'data/BAMS.csv',
        self.scrapper = scraper
        self.location = location
        self.time = time_slot

# Econ history:
# table element: everything under #parent-fieldname-text > div > table

# rockwool
