from src.Spider import Spider

spider = Spider()
spider.scrap("a", "Navigation")
qualification_types = spider.get_entry()

spider.scrap("a", "Navigation")
qualifications = spider.get_entry()
for qualification in qualifications:
    print(qualification)