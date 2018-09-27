from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from Collection.Crawler import crawling


def crawling_pelicana():
    for page in range(1, 116):
        html = crawling("http://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d"%page)

        bs = BeautifulSoup(html, "html.parser")
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]

            print("%s : %s" %(name, address))

def crawling_nene():
    pass

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()

    # nene
    crawling_nene()

    # kyochon

    # goobne