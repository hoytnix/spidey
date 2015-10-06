#!/usr/bin/env python

'''
py3k: True
'''

import sys
import requests
import zlib

from threading import Thread
from queue import Queue

from search_engine.toolbox.lines  import Lines
from search_engine.toolbox.sekret import _ARCHIVE_DIR, _DUMPS_DIR, _DOMAINS_FILE

''' Why aren't these input instead of global variables? '''
_all_pages = [ 
    #'contact', 
    #'contact-us',
    #'contactus',
    #'talk-to-us',
    #'contact_us',
    #'talk_to_us',
    #'contacts',
    'robots.txt',
    'sitemap.xml',
    'about',
    'about-us',
    'legal',
    'privacy',
    'privacy-policy',
    'feed',
]
_status_white = (200, 301, 302)

class Check:
    def __init__(self, url):
        self.url = url

    def save_page(self, page):
        try:
            _dir = None
            if page == '':
                _dir = 'index'
            elif page == 'robots.txt':
                _dir = 'robots'
            elif page == 'sitemap.xml':
                _dir = 'sitemap'
            else:
                _dir = page
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; idgaf/1.0; +http://idgaf.me)',
                'From': 'scan-admin@idgaf.me'
            }

            r = requests.get('http://%s/%s' % (self.url, page), headers=headers)
            html = r.content
            html = zlib.compress(html)
            with open('%s%s/%s' % (_DUMPS_DIR, _dir, self.url), 'wb+') as f:
                f.write(html)
        except:
            print('Unexpected error: %s' % sys.exc_info()[0])
            pass

    def status(self, page, t=10.0):

        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; idgaf/1.0; +http://idgaf.me)',
            'From': 'scan-admin@idgaf.me'
        }

        try:
            # Get Header.
            r = requests.head('http://%s/%s' % (self.url, page), timeout=t, headers=headers)
            return r.status_code
        except:
            #print 'Unexpected error:', sys.exc_info()[0]
            return None

class Work:
    def __init__(self, threads = 100, offset = 0, timeout = 15.0):
        self.lines = Lines(f=_DOMAINS_FILE)
        self.num_lines = len(self.lines.d)
        
        self.concurrent = threads
        self.timeout = timeout
        
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
            index = c.status(page='', t = self.timeout)
            if index and index in _status_white:
                print (_domain, end=' ')
                print ('/', end=' ')
                print (index)
                #c.save_page(page='')    

                for page in _all_pages:
                    status = c.status(page=page, t = self.timeout)
                    if status in _status_white:
                        print (_domain, end=' ')
                        print (page, end=' ')
                        print (status)
                        c.save_page(page=page)

            self.q.task_done()

def test():
    c = Check(url = '000game.biz')
    c.save_page(page='robots.txt')

if __name__ == '__main__':
    pass