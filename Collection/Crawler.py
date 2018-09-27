from datetime import datetime
from urllib.request import Request, urlopen


def crawling(url='', encoding='utf-8'):
    try:
        request = Request(url)                  # url을 통해서 요청을 진행한다.
        response = urlopen(request)             # 요청한 서버에서 응답을 받는다.

        try:
            receive = response.read()           # 받은 데이터를 receive 변수에 읽어드린다.
            result = receive.decode(encoding)   # 읽어드린 데이터를 미리 지정해둔 코드로 인코딩한다.
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')    # 만약 지정해준 인코딩에 제대로 되지않는다면 라이브러리에게 알아서 인코딩을 대체하도록 만든다.

        print("%s : success for request [%s]" % (datetime.now(), url))
        return result
    except Exception as e:
        print("%s : %s" %(e, datetime.now()))       # 예외 처리
