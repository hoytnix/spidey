#!/usr/bin/env python

'''
py3k: True
'''

'''
All run-time procedures should be here!
'''

import argparse
from os import walk
import importlib
from time import time

from search_engine.toolbox.sekret import _ARCHIVE_DIR, _DUMPS_DIR, _DOMAINS_FILE

# ------------------------------------------------------------------------------

parser = argparse.ArgumentParser(
    description = 'For determining the obstensible commerical viability of a website.',
    epilog = 'Copyright (c) Michael Hoyt 2015. All rights reserved.')

mode = parser.add_mutually_exclusive_group()

mode.add_argument('--page_checker', 
    help='page checker mode', 
    action='store_true'
)

mode.add_argument('--search', 
    help='search mode', 
)

mode.add_argument('--ips', 
    help='ip scraper mode', 
    action='store_true'
)



parser.add_argument('--threads',
    help='# of threads',
    type=int,
    default=10,
)

parser.add_argument('--offset',
    help='offset from start of index',
    type=int,
    default=0,
)

parser.add_argument('--timeout',
    help='timeout float for requests',
    type=float,
    default=15.0,
)

parser.add_argument('--file',
    help='specify a file input',
)

parser.add_argument('--test', 
    help='enable testing for an mode', 
    action='store_true'
)

args = parser.parse_args()

# ------------------------------------------------------------------------------

def get_files():
    _dirs  = []
    _files = []

    toor = True
    for root, dirs, files in walk(_ARCHIVE_DIR):
        if toor:
            _dirs = dirs
            toor = False
        root = root.replace('%s/' % _ARCHIVE_DIR, '')
        for f in files:
            #_files.append('%s%s' % (root, f))
            _files.append(f)
    return _files

def search_mode():
    from search_engine.search.search import Search
    
    s = Search(query=args.search)

def ip_check_mode():
    from search_engine.spider.ips import Work, test

    if args.test:
        test()
    else:
        w = Work(
            threads = args.threads, 
            offset = args.offset, 
            timeout = args.timeout,
        )

def page_check_mode():
    from search_engine.spider.page_checker import Work, test
    
    if args.test:
        test()
    else:
        w = Work(
            threads = args.threads, 
            offset = args.offset, 
            timeout = args.timeout,
        )

# ------------------------------------------------------------------------------

def main():

    if args.search:
        search_mode()

    elif args.page_checker:
        page_check_mode()

    elif args.ips:
        ip_check_mode()

    else:
        print('Hello, world!')

if __name__ == '__main__':
    start = time()
    main()
    print(time() - start)