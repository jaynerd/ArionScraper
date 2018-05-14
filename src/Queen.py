import timeit

from src.Spider import Spider

start = timeit.default_timer()

spider = Spider()

spider.scrap_urls()
print("Qualification types:")
print(spider.scrap_entries())
spider.clean_up(True)

spider.scrap_urls()
print("Qualifications:")
print(spider.scrap_entries())
spider.clean_up(True)

spider.scrap_urls()
spider.clean_up(False)

spider.scrap_urls()
paper_list = spider.scrap_entries()
return_text = "Returning to Qualification Details"
while return_text in paper_list:
    paper_list.remove(return_text)
print("Papers:")
print(paper_list)

paper_dict = {}
paper_dict = spider.sort_entries(paper_list)
print("Sorted papers:")
print(paper_dict)
spider.clean_up(True)
end = timeit.default_timer()

paper_dict = spider.scrap_requisites(paper_dict)
print("Sorted papers with requisites:")
print(paper_dict)

print(end - start)
