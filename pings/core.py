import requests, time, zlib, sys
from time import strftime
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from sekret import _DUMPS_DIR, _BLACK_LIST

def download(url, engine):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; idgaf/1.0; +http://idgaf.me)',
            'From': 'scan-admin@idgaf.me'
        }

        r = requests.get(url, headers=headers)
        html = r.content

        file_path = '%s/%s/%s' % (_DUMPS_DIR, engine, strftime("%Y%m%d-%H%M%S"))
        with open(file_path, 'wb+') as f:
            f.write(html)

        return file_path
    except:
        print("Unexpected error: %s" % sys.exc_info()[0])
        return False

def google():
    url = 'http://blogsearch.google.com/changes.xml?last=60'
    engine = 'google'
    return download(url = url, engine = engine)

def yandex():
    url = 'http://ping.blogs.yandex.ru/changes.xml'
    engine = 'yandex'
    return download(url = url, engine = engine)

def weblogs():
    url = 'http://rpc.weblogs.com/changes.xml'
    engine = 'weblogs'
    return download(url = url, engine = engine)

def extract(_file):
    #New URLs
    new = []

    tree = ET.parse(_file)
    root = tree.getroot()
    for child in root:
        try:
            url = urlparse( child.attrib['url'] )[1]

            # Validate, please.
            b = True
            if '.' not in url:
                b = False
            for x in _BLACK_LIST:
                if x in url:
                    b = False
            if len(url.split('.')) > 3:
                b = False

            if b:
                if url[:4] == 'www.':
                    url = url[4:]
                new.append(url)
        except:
            pass #no russian! :D

    #Add
    new = sorted(set(new))
    with open(_file, 'w+') as f:
        i = 0
        for url in new:
            if i == new.__len__() - 1:
                f.write(url)
            else:
                f.write(url+'\n')
            i += 1

# ------------------------------------------------------------------------------

def test():
    f = google()
    if f:
        extract(_file = f)
    else:
        print("Failed.")

if __name__ == '__main__':
    test()