# define a class called seminar
# import packages needed for the class

class seminar:
    '''
    this class is used to process the data that we scrape from the seminar websites
    goal is to retrieve the future seminars with date and title announced
    approach: save a local version and then compare it with the newly scrapped data?
    '''
    
    def __init__(self, url, name, path, scraper, location, time_slot, semester):
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
        self.path = path
        self.scrapper = scraper
        self.location = location
        self.time = time_slot
        self.semester = semester