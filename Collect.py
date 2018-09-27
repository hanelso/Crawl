from itertools import count
from bs4 import BeautifulSoup
from Collection.Crawler import crawling
import pandas as pd

RESULT_DIRECTORY = "__result__"

def crawling_pelicana():
    results = []
    for page in count(start=1):
        html = crawling("http://www.pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d"%page)

        bs = BeautifulSoup(html, "html.parser")                     # BeautifulSoup으로 html 핸들링 라이브러리 이용.
        tag_table = bs.find('table', attrs={'class': 'table mt20'}) # 받아온 html 문자열에서 table중에 class명이 'table mt20'인 것만 찾는다.
        tag_tbody = tag_table.find('tbody')                         # table 안에서 tbody태그들만 찾는다.
        tags_tr = tag_tbody.findAll('tr')                           # tbody 안에서 tr 태그들만을 모두 찾는다.

        # 페이지의 끝 확인
        if len(tags_tr) == 0:
            break

        # tr 태그들을 하나씩 보면서 data들을 얻어낸다.
        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            results.append((name, address))                 # 데이터의 형식을 튜플형으로(name, address)로 받는다.

    # 데이터의 저장
    table = pd.DataFrame(results, columns=['name', 'address'])      # pandas는 데이터를 자료구조화 시켜주는 라이브러리
    # print(table['name'])
    # print(table['address'])
    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    # csv파일로 받은 데이터를 자료구조화 시켜서 저장한다. ( 자바의 해시테이블 처럼)


def crawling_nene():
    pass

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()

    # nene
    crawling_nene()

    # kyochon

    # goobne