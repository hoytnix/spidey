root_path = '/home/johnny/datas/my_arch/'
pages = [
    'contact',
    'contact-us',
    'contact_us',
    'contacts',
    'contactus',
    'index',
    'talk-to-us',
    'talk_to_us',
]

from os import walk, remove as osremove, path as ospath
from time import time

from domain_parse import dumps_to_db

def get_dumps(page):
    page_path = '%s%s' % (root_path, page)
    for root, dirs, files in walk(page_path):
        return files

def clean_tlds(page):
    from lists.black import black_tlds as tlds

    page_path = '%s%s' % (root_path, page)
    
    files = get_dumps(page)
    print(files.__len__())

    for f in files:
        b = False
        for s in tlds:
            if f[f.__len__() - s.__len__():] == s:
                b = True
                break
        if b:
            file_path = '%s/%s' % (page_path, f)
            osremove(file_path)

    files = get_dumps(page)
    print(files.__len__())

def clean_subdomains(page):
    from lists.black import subdomains
    
    page_path = '%s%s' % (root_path, page)

    files = get_dumps(page)
    print(files.__len__())

    for f in files:
        b = False
        for s in subdomains:
            if s in f:
                b = True
                break
        if b:
            file_path = '%s/%s' % (page_path, f)
            osremove(file_path)

    files = get_dumps(page)
    print(files.__len__())

def subdomains(page='index'):
    # Muh logix.
    i = 0
    db = dumps_to_db(get_dumps(page))

    sorted_db = sorted(db, key=lambda k: len(db[k]['subdomains']), reverse=True)
    
    xxx = []
    i = 0
    for x in sorted_db:
        row = db[x]['subdomains']
        if row.__len__() > 100:
            i += 1
            xxx.append(x)
            print(i, end=' ')
            print(x)

    print('-' * 40)

    for x in xxx:
        print("    '%s'," % x)

# -------------------------------------

def test():
    d = {"one": { 'subdomains': [(1,3),(1,4)] },"two": { 'subdomains': [(1,2),(1,2),(1,3)] },"three": { 'subdomains': [(1,1)] }}
    d = sorted(d, key=lambda k: len(d[k]['subdomains']), reverse=True)
    print(d)
    for x in d:
        print(x)

if __name__ == '__main__':
    
    start = time()
    
    #test()
    
    #subdomains()
    
    for page in pages:
        print(page)
        #clean_subdomains(page)
        clean_tlds(page)
        print('-' * 10)

    print(time() - start)