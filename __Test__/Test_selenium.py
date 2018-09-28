import time

from selenium import webdriver

# Selenium을 이용한 웹 브라우져 객체를 생성해서 구글 홈페이지를 띄운다.

wd = webdriver.Chrome('H:/국기3/IoT2018/chromedriver/chromedriver.exe')   # wd로 웹브라우져 객체를 생성
wd.get('http://www.google.com') #구글 url을 줘서 접속
time.sleep(10)  # 웹 브라우져가 10초동안 유지 되도록

html = wd.page_source       # 웹 브라우져의 html 소스코드를 가져온다.
print(html)

wd.quit()           # 웹 브라우져 종료(닫기)
