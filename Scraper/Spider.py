import urllib3
from bs4 import BeautifulSoup
from typing import List


class Spider:
    base_url: str
    given_url: str
    scraped_partial_urls: [str]

    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.http = urllib3.PoolManager()
        self.base_url = None
        self.given_url = None
        self.scraped_partial_urls = None

    def set_base_url(self, base_url):
        self.base_url = base_url

    def set_given_url(self, given_url):
        self.given_url = given_url

    def scrap_partial_urls(self):
        request = self.http.request("GET", self.base_url + self.given_url)
        soup = BeautifulSoup(request.data, "lxml")
        self.scraped_partial_urls = soup.find_all("a", "Navigation")

    def scrap_entries(self):
        scraped_entries: List[str] = []
        for a_tag in self.scraped_partial_urls:
            scraped_entries.append(a_tag.text)
        return scraped_entries

    def scrap_paper_entries(self):
        scraped_entries: List[str] = []
        counter = 0
        for a_tag in self.scraped_partial_urls:
            if counter != 0:
                scraped_entries.append(a_tag.text)
            counter += 1
        return scraped_entries

    def scrap_links(self):
        scraped_links: List[str] = []
        for link in self.scraped_partial_urls:
            link = link.get("href")
            scraped_links.append(link)
        return scraped_links

    def scrap_table_of_paper_link(self):
        scraped_link = self.scraped_partial_urls[0].get("href")
        return scraped_link

    def scrap_paper_links(self):
        scraped_links: List[str] = []
        counter = 0
        for link in self.scraped_partial_urls:
            if counter != 0:
                link = link.get("href")
                scraped_links.append(link)
            counter += 1
        return scraped_links
