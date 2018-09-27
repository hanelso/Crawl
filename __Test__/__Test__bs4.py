from bs4 import BeautifulSoup

html = '<td class="title black"><div class="tit3 black" id="t3" name="t3">'\
    '<a href="/movie/bi/mi/basic.nhn?code=163533" title="안시성">안시성</a>' \
    '</div></td>'

# 1. Tag 이름으로 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs), end="\n\n")

    tag = bs.td     # td tag를 뽑아온다. 소름...
    print(tag)      # tag 조회

    tag = bs.div    # div tag를 뽑아온다.
    print(tag)      # tag 조회

    tag = bs.a
    print(tag)

    #한번에 태그를 뽑아오기
    print("==" * 100)
    print(bs)
    print(bs.div)
    print(bs.div.a)


# 2. Attributes 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    print(tag['id'])
    print(tag.attrs)

    # print(tag.name)
    # print(tag['name'])

# 3. attr로 조회하기
def ex3():
    bs = BeautifulSoup(html,'html.parser')

    tags = bs.find('td', attrs={'class': 'title'})
    print(tags)

    tags = bs.find(attrs={'title': '안시성'})
    print(tags)

    tags = bs.find('a')
    print(tags)

if __name__ == '__main__' :
    ex1()
    print()
    ex2()
    print()
    ex3()
