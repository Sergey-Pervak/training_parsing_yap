import requests_cache
from bs4 import BeautifulSoup


DOWNLOADS_URL = 'https://docs.python.org/3/download.html '

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    necessary_files = soup.find('table', attrs={'class': 'docutils'})
    td_tags = necessary_files.find_all('td')
