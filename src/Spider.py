import re
import urllib3
from bs4 import BeautifulSoup

base_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/'
initial_url = 'QualificationTypes.aspx'


class Spider:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.http = urllib3.PoolManager()
        self.target_urls = []
        self.scraped_urls = []
        self.target_urls.append(initial_url)
        self.title = ""

    def scrap_urls(self):
        for url in self.target_urls:
            request = self.http.request("GET", base_url + url)
            soup = BeautifulSoup(request.data, "lxml")
            for partial_url in soup.find_all("a", "Navigation"):
                self.scraped_urls.append(partial_url)

    def scrap_entries(self):
        target_entries = []
        for tag in self.scraped_urls:
            target_entries.append(tag.text)
        return target_entries

    def scrap_requisites(self, dictionary):
        for url in self.target_urls:
            request = self.http.request("GET", base_url + url)
            soup = BeautifulSoup(request.data, "lxml")
            self.title = soup.find("td", {"class": "TitlePage"})
            requisites = soup.find_all("a", id=re.compile("^wucControl_repQualifications__ctl1_wucPaperRequisites"))
            for tag in requisites:
                if self.title in dictionary:
                    temp_list = dictionary[self.title]
                    if tag.text not in temp_list:
                        dictionary[self.title].append(tag.text)
                        print (dictionary)
        return dictionary

    def sort_entries(self, entries):
        dictionary = {}
        counter = 0
        for i in range(0, int(len(entries) / 2)):
            dictionary.setdefault(entries[(counter + 1)], [])
            temp_list = dictionary[entries[(counter + 1)]]
            if entries[counter] not in temp_list:
                dictionary[entries[(counter + 1)]].append(entries[counter])
            counter += 2
        return dictionary

    def clean_up(self, is_refined):
        self.target_urls.clear()
        for url in self.scraped_urls:
            url = url.get("href")
            if not is_refined:
                url = url.replace("../", "")
            self.target_urls.append(url)
        self.scraped_urls.clear()
