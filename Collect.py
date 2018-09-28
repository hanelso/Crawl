import time
from datetime import datetime
from itertools import count
from bs4 import BeautifulSoup
from selenium import webdriver

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

    result = []

    # 시작과 끝이 있으면 range, 없으면 count
    for page in count(start = 1):
        html = crawling('https://nenechicken.com/17_new/sub_shop01.asp?page={}&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'.format(page))
        bs = BeautifulSoup(html, 'html.parser')
        tags_div = bs.findAll('div', attrs={'class':'shopInfo'})

        for tag_div in tags_div:
            shopname = tag_div.find('div', attrs={'class':'shopName'}).text
            shopaddress = tag_div.find('div', attrs={'class':'shopAdd'}).text
            result.append((shopname, shopaddress))

        if(len(tags_div)<24):
            break

    # Strore
    table = pd.DataFrame(result, columns=['name', 'address'])
    table.to_csv('{0}/nene_table.csv'.format(RESULT_DIRECTORY),encoding='utf-8',mode='w', index=True)
    #print(table)

def crawling_kyochon():

    results = []

    # 시작과 끝이 있으면 range, 없으면 count
    for sido1 in range(1,2):
        for sido2 in count(start=1):
            url = ('http://www.kyochon.com/shop/domestic.asp?sido1={}&sido2={}&txtsearch='.format(sido1, sido2))
            html = crawling(url)

            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul =bs.find('ul', attrs={'class':'list'})

            for tag_a in tag_ul.findAll('a'):
                tag_dt = tag_a.find('dt')
                if tag_dt is None:
                    break
                name = '' if tag_dt is None else tag_dt.get_text()
                address = tag_a.find('dd').getText().strip().split('\r\n')
                for index, string in enumerate(address):
                    address[index] = string.strip('\t')
                results.append((name, address))

    table = pd.DataFrame(results, columns=['name', 'address'])
    table.to_csv('{0}/KyoChon_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    #print(results)

# GoobNe 같은 경우에는 JavaScript로 페이지를 Dom화 시켰기때문에 JavaScript를 실행한 후 소스를 가져와야한다.
# 순서 : 페이지 loading -> JavaScript 실행 -> HTML Source 가져오기
def crawling_goobne():
    url = "http://www.goobne.co.kr/store/search_store.jsp"

    # 페이지 로딩
    wd = webdriver.Chrome('H:/국기3/IoT2018/chromedriver/chromedriver.exe')  # wd로 웹브라우져 객체를 생성
    wd.get(url)
    time.sleep(1)

    results = []

    for page in count(start=1):

        # Java Script 실행
        script = 'store.getList({})'.format(page)
        wd.execute_script(script)
        print("%s : success for request [%s]" % (datetime.now(), page))
        time.sleep(1)

        # Java Script 실행 결과 HTML(랜더링된 HTML) 가져오기
        html = wd.page_source
        #print(html)

        # parsing with bs4
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id':"store_list"})
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)

            name = strings[1]
            address = strings[6]

            results.append((name, address))

    table = pd.DataFrame(results, columns=['name', 'address'])
    table.to_csv('{0}/GoobNe_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)

    wd.quit()
   # print(results)
if __name__ == '__main__':
    # pelicana
    #crawling_pelicana()

    # nene
    #crawling_nene()

    # kyochon
    crawling_kyochon()

    # goobne
    #crawling_goobne()