from src.Spider import Spider


class Queen:

    def __init__(self):
        self.spider = Spider()

    def dispatch_spider(self, tag_a, tag_b):
        self.spider.scrap(tag_a, tag_b)

    def collect_information(self):
        brain = self.spider.get_entries()
        return brain

    def washout_spider(self):
        self.spider.clean_up_urls()


queen = Queen()

queen.dispatch_spider("a", "Navigation")
queen.washout_spider()

queen.dispatch_spider("a", "Navigation")
queen.washout_spider()

queen.dispatch_spider("a", "Navigation")
queen.washout_spider()
