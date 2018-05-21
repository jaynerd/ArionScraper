
# initialization
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
target_urls = []
scrapped_urls = []

# start scraping the study options page
def scrap_study_option_urls():
    for url in target_urls:
        request = http.request('GET', url)
        soup = BeautifulSoup(request.data, 'lxml')
        div = soup.find_all('div', {'class': 'col-sm-6'})
        counter = 0
        for element in div:
            a = element.find_all('a')
            for url in a:
                url = url.get('href')
                scrapped_urls.append(url)
            counter += 1
            if counter == 2:
                break
				
# scrapping nested links of study options
target_urls.append('https://www.aut.ac.nz/study/study-options')
scrap_study_option_urls()
target_urls.clear()
for url in scrapped_urls:
    target_urls.append(url)
    print(url)
scrapped_urls.clear()

def scrap_undergraduate_degrees():
    for url in target_urls:
        request = http.request('GET', url)
        soup = BeautifulSoup(request.data, 'lxml')
        div = soup.find_all('div', {'class': 'panel-body'})
        for element in div:
            a = element.find_all('a')
            for url in a:
                url = url.get('href')
                scrapped_urls.append(url)
                print(url)
            break
			
			
scrap_undergraduate_degrees()