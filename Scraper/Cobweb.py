from typing import List

from Scraper.Spider import Spider

base_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/'
initial_url = 'QualificationTypes.aspx'


class Cobweb:
    def create_spider(self):
        spider = Spider()
        return spider

    def set_base_url(self, spider, url):
        spider.set_base_url(url)

    def set_given_url(self, spider, url):
        spider.set_given_url(url)


# thread starts here
# spider instantiation
cobweb = Cobweb()
tarantula = cobweb.create_spider()

# setting initial url
cobweb.set_base_url(tarantula, base_url)
cobweb.set_given_url(tarantula, initial_url)

# scraping starts here
# get qualification types
tarantula.scrap_partial_urls()
qualification_types = tarantula.scrap_entries()
qualification_type_links = tarantula.scrap_links()

# get qualifications
qualifications = []
qualification_links = []
for link in qualification_type_links:
    cobweb.set_given_url(tarantula, link)
    tarantula.scrap_partial_urls()
    qualification_entries = tarantula.scrap_entries()
    qualification_inner_links = tarantula.scrap_links()
    qualifications.append(qualification_entries)
    for qualification_inner_link in qualification_inner_links:
        qualification_links.append(qualification_inner_link)

# get papers
papers = []
paper_links = []
for link in qualification_links:
    cobweb.set_given_url(tarantula, link)
    tarantula.scrap_partial_urls()
    table_of_paper_link = tarantula.scrap_table_of_paper_link()
    table_of_paper_link = table_of_paper_link.replace("../", "")

    cobweb.set_given_url(tarantula, table_of_paper_link)
    tarantula.scrap_partial_urls()
    paper_entries = tarantula.scrap_paper_entries()
    paper_inner_links = tarantula.scrap_paper_links()
    papers.append(paper_entries)

    counter = 0
    for paper_inner_link in paper_inner_links:
        counter %= 2
        if counter == 0:
            paper_links.append(paper_inner_link)
        counter += 1

paper_code_list: List[str] = []
paper_list: List[str] = []
for entry in papers:
    for paper in entry:
        paper_array = paper.split(",")
        counter = 0
        for single_paper in paper_array:
            counter %= 2
            print(single_paper)
            if counter == 0:
                paper_code_list.append(single_paper)
            else:
                paper_list.append(single_paper)
            counter += 1
