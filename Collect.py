from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from Collection.Crawler import crawling
import pandas as pd

RESULT_DIRECTORY = "__result__"

def crawling_pelicana():
    results = []
    for page in count(start=1):
        html = crawling("http://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d"%page)

        bs = BeautifulSoup(html, "html.parser")
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 페이지의 끝 확인
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]

            results.append((name, address))

    # 데이터의 저장
    table = pd.DataFrame(results, columns=['name', 'address'])
    # print(table['name'])
    # print(table['address'])
    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)


def crawling_nene():
    pass

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()

    # nene
    crawling_nene()

    # kyochon

    # goobne