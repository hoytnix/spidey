from os import walk
from time import time
import zlib
import re
from random import randint


import subprocess as sp
from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

from time import strftime


from BeautifulSoup import BeautifulSoup as bs4

from jsondb import Jsondb as DB
from secret import DUMPS_DIR

class Work:
    def __init__(self):
        
        # Initialize Database
        self.dbs = 70
        self.new_db()
        self.db = DB(f='./json/forms/forms-%d.json' % self.dbs)
        self.json = {}

        # Stuff
        self.txt = ''
        self.sites = self.get_files()
        self.lines = len(self.sites)
        self.concurrent = 1
        self.q = Queue(self.concurrent * 2)
        for self.i in range(self.concurrent):
            self.t = Thread(target=self.doWork)
            self.t.daemon = True
            self.t.start()
        try:
            for self.i in xrange(self.dbs * 2000, self.lines):
                self.q.put(self.i)
            self.q.join()
        except KeyboardInterrupt:
            sys.exit(1)

    def new_db(self):
      with open('./json/forms/forms-%d.json' % self.dbs, 'w+') as f:
        f.write('{}')

    def doWork(self):
        while True:
            self.domain = int(self.q.get())
            self.txt = self.get_txt(self.domain)

            try:
              self.s = self.search_forms(txt = self.txt)
              if self.s:
                self.json[self.sites[self.domain]] = self.s
            except:
              pass

            if len(self.json) % 50 == 0:
              print strftime('%H:%S')

            if len(self.json) == self.lines - 150000 - 2:
              self.db.update(self.json)
              self.db.save()
              self.dbs += 1
              #self.new_db()
              self.db = DB(f='./json/forms/forms-%d.json' % self.dbs)
              self.json = {}

            self.q.task_done()    

    def control(self, c):
      name     = c.get('name')
      _id      = c.get('id')
      action   = c.get('action')
      method   = c.get('method')
      _class   = c.get('class')
      _type    = c.get('type')
      disabled = c.get('disabled')

      control = {}
      if name:
        control['name'] = name

      if _id:
        control['id'] = _id

      if action:
        control['action'] = action

      if method:
        control['method'] = method

      if _class:
        control['class'] = _class

      if _type:
        control['type'] = _type

      if disabled:
        control['disabled'] = disabled

      return control

    def search_forms(self, txt):

      # Soup Object
      self.soup = bs4(txt)

      self.forms = self.soup.findAll('form')
      self.form_len = len(self.forms)

      if self.form_len < 0:
        return False
        
      self.site = {}

      self.i = 0
      for self.form in self.forms:
        self._f = self.control(self.form)

        self._key = str(self.i)

        self.site[self._key] = {}

        for self.key in self._f:
          self.site[self._key][self.key] = self._f[self.key]

        self.inputs = self.forms[self.i].findAll('input')
        self.site[self._key]['inputs'] = []
        for self._input in self.inputs:
          self._in = {}
          self._i = self.control(self._input)
          for self.key in self._i:
            self._in[self.key] = self._i[self.key]
          self.site[self._key]['inputs'].append(self._in)

        self.i += 1

      return self.site

    def get_txt(self, domain):
      # Read Data.
      cd = ''
      with open('%s/%s' % ( DUMPS_DIR, self.sites[domain]), 'r') as f:
        cd = f.read()

      # Decompress
      return zlib.decompress(cd)

    def get_files(self):
      txt = ''
      with open('../dumps/04-forms', 'r') as f:
        txt = f.read()

      # Sanatize.
      txt = txt.split('-' * 100)
      txt = txt[1]
      txt = txt.split('-' * 5)[:-1]

      i = 0
      for x in txt:
        txt[i] = txt[i].strip()
        i += 1

      for x in txt:
        if x == '':
          txt.remove('')

      # Search.
      sites = []
      for site in txt:
        sites.append( site.split('\n')[-1].replace('file: ', '') )

      return sites


def save(url, page):
    with open('../dump', 'a') as f:
        f.write(url + '/' + page[0] + '\n')

def main():
  w = Work()

if __name__ == '__main__':
  m = main()