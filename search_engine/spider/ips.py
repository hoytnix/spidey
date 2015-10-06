#!/usr/bin/env python

'''
py3k: True
'''

import sys
import requests

from threading import Thread
from queue import Queue

from search_engine.toolbox.lines  import Lines
from search_engine.toolbox.sekret import _ARCHIVE_DIR, _DUMPS_DIR, _DOMAINS_FILE

import http.client

def getresponse(self,*args,**kwargs):
    response = self._old_getresponse(*args,**kwargs)
    if self.sock:
        response.peer = self.sock.getpeername()
    else:
        response.peer = None
    return response

http.client.HTTPConnection._old_getresponse = http.client.HTTPConnection.getresponse
http.client.HTTPConnection.getresponse = getresponse

def save(domain, ip):
    with open('/opt/datas/ips', 'a') as f:
        f.write('%s|%s\n' % (domain, ip))

class Check:
    def __init__(self, url):
        self.url = url
        self.r   = self.response()
        if self.r:
            self.ip  = self.check_peer(resp=self.r)
        else:
            self.ip  = False

    def response(self):
        try:
            return requests.head('http://' + self.url)
        except:
            return False

    def check_peer(self, resp):
        orig_resp = resp.raw._original_response
        if hasattr(orig_resp,'peer'):
            return getattr(orig_resp,'peer')

class Work:
    def __init__(self, threads = 100, offset = 0, timeout = 15.0):
        self.lines = Lines(f=_DOMAINS_FILE)
        self.num_lines = len(self.lines.d)
        self.concurrent = threads
        self.q = Queue(self.concurrent * 2)
        for self.i in range(self.concurrent):
            self.t = Thread(target=self.doWork)
            self.t.daemon = True
            self.t.start()
        try:
            for self.i in range(offset, self.num_lines):
                self.q.put(self.i)
            self.q.join()
        except KeyboardInterrupt:
            sys.exit(1)

    def doWork(self):
        while True:
            n = int(self.q.get())
            _domain = self.lines.find_line(n=n)

            c = Check(url = _domain)
            ip = c.ip
            if ip:
                print(ip, end = ' ')
                print(_domain)
                save(ip=ip, domain=_domain)

            self.q.task_done()

def test():
    c = Check(url='http://google.com')
    print(c.ip)

if __name__ == '__main__':
    pass