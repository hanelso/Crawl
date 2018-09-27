from datetime import datetime
from urllib.request import Request, urlopen


def crawling(url='', encoding='utf-8'):
    try:
        request = Request(url)
        response = urlopen(request)

        try:
            receive = response.read()
            result = receive.decode(encoding)
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        print("%s : success for request [%s]" % (datetime.now(), url))
        return result
    except Exception as e:
        print("%s : %s" %(e, datetime.now()))
