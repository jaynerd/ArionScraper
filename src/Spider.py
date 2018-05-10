import urllib3
from bs4 import BeautifulSoup

base_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/'
initial_url = 'QualificationTypes.aspx'


class Spider:
    # Initialization
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.http = urllib3.PoolManager()
        self.given_url = []
        self.scraped_url = []
        self.scraped_entry = []
        self.base_url = base_url
        self.given_url.append(initial_url)

    # Starts scraping
    def scrap(self, tag_a, tag_b):
        # Scraping inner urls
        for url in self.given_url:
            request = self.http.request("GET", base_url + url)
            soup = BeautifulSoup(request.data, "lxml")
            self.scraped_url = soup.find_all(tag_a, tag_b)

        # Scraping entry texts
        for tag in self.scraped_url:
            self.scraped_entry.append(tag.text)

    # Returns collected entries to the queen
    def get_entry(self):
        target_entry = self.scraped_entry
        self.given_url.clear()
        for url in self.scraped_url:
            self.given_url.append(url)
        self.scraped_url.clear()
        return target_entry
