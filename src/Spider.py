import urllib3
from bs4 import BeautifulSoup

base_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/'
initial_url = 'QualificationTypes.aspx'


class Spider:
    # Initialization
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.http = urllib3.PoolManager()
        self.given_urls = []
        self.scraped_urls = []
        self.scraped_entries = []
        self.base_url = base_url
        self.given_urls.append(initial_url)

    # Start scraping
    def scrap(self, tag_a, tag_b):
        # Scraping inner urls
        for url in self.given_urls:
            request = self.http.request("GET", base_url + url)
            soup = BeautifulSoup(request.data, "lxml")
            for result in soup.find_all(tag_a, tag_b):
                self.scraped_urls.append(result)

        # Scraping entry texts
        for tag in self.scraped_urls:
            self.scraped_entries.append(tag.text)

    # Returns collected entries to the queen
    def get_entries(self):
        target_entries = []
        for entry in self.scraped_entries:
            target_entries.append(entry)
        return target_entries

    # Refines collected urls to working links without unnecessary tags
    # Clears values from previous extractions to avoid any duplicates
    def refine_urls(self):
        self.given_urls.clear()
        self.scraped_entries.clear()
        for url in self.scraped_urls:
            url = url.get("href")
            self.given_urls.append(url)
        self.scraped_urls.clear()
