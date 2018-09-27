from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
response = urlopen(request)
html = response.read().decode("cp949")

# print(html)

bs = BeautifulSoup(html, "html.parser")
#print(bs.prettify)                                      #이쁘게 보기...

tags = bs.findAll('div', attrs={'class': "tit3"})
for index, tag in enumerate(tags):
    print(index, tag.a.text, tag.a['href'], sep=' - ')