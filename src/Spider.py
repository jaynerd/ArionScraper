import urllib3
from bs4 import BeautifulSoup

base_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/'
initial_url = 'QualificationTypes.aspx'


class Spider:
    # Initialization
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.http = urllib3.PoolManager()
        self.target_urls = []
        self.scraped_urls = []
        self.scraped_entries = []
        self.base_url = base_url
        self.target_urls.append(initial_url)

    # Start scraping
    def scrap(self, tag_a, tag_b):
        # Scraping nested urls
        for url in self.target_urls:
            request = self.http.request("GET", base_url + url)
            soup = BeautifulSoup(request.data, "lxml")
            for result in soup.find_all(tag_a, tag_b):
                self.scraped_urls.append(result)

    # Returns scraped entries to the queen
    def get_entries(self):
        target_entries = []
        for tag in self.scraped_urls:
            target_entries.append(tag.text)
        return target_entries

    # Refines collected urls to working links without unnecessary tags
    # Clears values from previous extractions to avoid any duplicates
    def clean_up_urls(self):
        self.target_urls.clear()
        self.scraped_entries.clear()
        for url in self.scraped_urls:
            url = url.get("href")
            self.target_urls.append(url)
        self.scraped_urls.clear()
