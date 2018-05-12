from src.Spider import Spider


class Queen:

    def __init__(self):
        self.spider = Spider()

    def dispatch_spider(self, tag_a, tag_b):
        self.spider.scrap(tag_a, tag_b)

    def dispatch_spider_on_task(self, dictionary):
        self.spider.scrap_requisites(dictionary)

    def collect_information(self):
        brain = self.spider.get_entries()
        return brain

    def washout_spider(self, is_refined):
        self.spider.clean_up_urls(is_refined)

    def make_dictionary(self, dictionary, contents):
        counter = 0
        for i in range(0, int(len(contents) / 2)):
            dictionary.setdefault(contents[counter + 1], [])
            dictionary[contents[counter] + 1].append(contents[counter])
            counter += 2


queen = Queen()

# Get qualification types
queen.dispatch_spider("a", "Navigation")
queen.washout_spider(True)

# Get qualifications
queen.dispatch_spider("a", "Navigation")
queen.washout_spider(True)

# Get table of papers
queen.dispatch_spider("a", "Navigation")
queen.washout_spider(False)

# Get papers
queen.dispatch_spider("a", "Navigation")
papers = queen.collect_information()
text = 'Returning to Qualification Details'
while text in papers:
    papers.remove(text)

# Make a dictionary of papers
dict_papers = {}
queen.make_dictionary(dict_papers, papers)
queen.washout_spider(True)

# Get pre-requisites
queen.dispatch_spider_on_task(dict_papers)
