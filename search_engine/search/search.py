from os     import walk
from time   import time
from zlib   import decompress
from random import randint
import re

from bs4 import BeautifulSoup as bs4

from search_engine.toolbox.sekret import _ARCHIVE_DIR

class Search:
    def __init__(self, query):
        self.options = self.args(query)
        self.files   = self.get_files()
        self.results = []

        for f in self.files:
            self.process_file(fp = f, options=self.options)

        print(self.results.__len__())

    def args(self, query):
        query = query.split(' ')

        options = {
            'options': {
                'inurl': False,
                'text':  False,
                'url':   False,
                'forms': False,
            },
            'text': []
        }

        if ':' in query[0]:
            if 'inurl:' in query[0]:
                options['options']['inurl'] = True
                options['text'] = query[0].split(':')[1]

        return options

    def process_file(self, fp, options):
        this_is_a_song_without_words = False

        key    = options['text']
        in_url = options['options']['inurl']
        txt    = options['options']['text']
        url    = options['options']['url']
        _fomrs = options['options']['forms']

        if txt or url:
            dd = self.decompress_file(fp=fp)

        if in_url:

            if key in fp.replace(_ARCHIVE_DIR, ''):
                this_is_a_song_without_words = True

        elif _forms:

            self.search_forms(key = key)

        elif txt and url:

            s = self.search_url(txt = dd, key = key)
            if s != False:
                this_is_a_song_without_words = True
                print(s)

        elif txt and not url:

            if key in dd:
                this_is_a_song_without_words = True

        # TUI:
        if this_is_a_song_without_words:
            self.results.append(fp)

    def get_files(self):
        _files = []
        for root, dirs, files in walk(_ARCHIVE_DIR):
            for f in files:
                #print('%s%s' % (root, f))
                _files.append('%s%s' % (root, f))
        return _files

    def decompress_file(self, fp, lower=False):
        # Read Data.
        cd = ''
        with open('%s%s' % ( _ARCHIVE_DIR, fp), 'rb') as f:
            cd = f.read()

        # Decompress
        dd = decompress(cd)
        dd = str(dd)
        if lower:
            dd = dd.lower()

        return dd

    def search_url(self, txt, key):
        
        i = re.search(key, txt, flags=re.IGNORECASE)
        
        if i:
        
            start = i.start(); end = i.end()

            txt_len = len(txt) - 1

            found = True
            while True:
                if end == start + 256 or end == txt_len:
                    found = False
                    break
                if txt[end] == '"' or txt[end] == '\'':
                    break
                end += 1

            _found_txt = txt[start:end]

            if found:

                boo = True

                while True:
                    if '\n' in _found_txt:
                        boo = False
                        break
                    for _neg in _negs:
                        if _neg in _found_txt:
                            boo = False
                            break
                    if not boo:
                        break
                    for _neg in _negs_equals:
                        if _found_txt == _neg:
                            boo = False
                            break
                    break

                return _found_txt if boo else False

        else:

            return False

    def search_forms(self, key='lol'):
        for db in forms:
            if len(db) < 0:
                pass

            for db_key in db:
                row = db[db_key]
                for c_key in row:
                    control = row[c_key]

                    boo = False
                    for t_key in control:
                        thing = control[t_key]

                        _input = type(thing) == type([])
                        _attr  = isinstance(thing, str) or isinstance(thing, unicode)

                        if _attr:
                            if key in thing:
                                try:
                                    d = [ {
                                        'word':       key,
                                        'row':     db_key,
                                        'control':  c_key,
                                        'thing':    t_key,
                                    } ]
                                    print(d)
                                except:
                                    pass

                        if _input:
                            pass