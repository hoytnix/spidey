from jsondb import Jsondb
from urlparse import urlparse
import operator

class DomainParts(object):
  def __init__(self, domain_parts, tld):
    self.domain = None
    self.subdomains = None
    self.tld = tld
    if domain_parts:
      self.domain = domain_parts[-1]
      if len(domain_parts) > 1:
        self.subdomains = domain_parts[:-1]

_tlds = [
  # Top-3
  'com', 'net', 'org',
  # Auth
  'gov', 'edu', 'mil',
  # Generic
  'info', 'biz', "mobi",
  # ccTLD
  'co.uk', 'ru', 'de', 'uk', 'jp', 'br', 'pl', 'in',
  'it', 'fr', 'cn', 'au', 'nl', 'ir', 'es', 'kr',
  'cz', 'eu', 'ca', 'ua', 'za', 'co', 'gr', 'ro',
  'se', "mx", "tw", "ch", "at", "dk", "tv", "vn",
  "be", "me", "tr", "us", "ar", "hu", "no", "sk",
  "fi", "cl", "id", "cc", "nz", "pt", "by", "il",
  "ie", "my", "kz", "sg", "hk", "lt", "io", "su",
  "pk", "bg", "tk", "th", "az", "pe", "lv", "hr",
  "ph", "ae", "rs", "ws", "si", "xyz", "pro", "ee",
]

def get_domain_parts(url, tlds=_tlds):
  urlElements = urlparse(url).hostname.split('.')
  # urlElements = ["abcde","co","uk"]
  for i in range(-len(urlElements),0):
    lastIElements = urlElements[i:]
    #    i=-3: ["abcde","co","uk"]
    #    i=-2: ["co","uk"]
    #    i=-1: ["uk"] etc

    candidate = ".".join(lastIElements) # abcde.co.uk, co.uk, uk
    wildcardCandidate = ".".join(["*"]+lastIElements[1:]) # *.co.uk, *.uk, *
    exceptionCandidate = "!"+candidate

    # match tlds: 
    if (exceptionCandidate in tlds):
      return ".".join(urlElements[i:]) 
    if (candidate in tlds or wildcardCandidate in tlds):
      return DomainParts(urlElements[:i], '.'.join(urlElements[i:]))
      # returns ["abcde"]

  raise ValueError("Domain not in global list of TLDs")

def get_dumps():
  dumps = []
  with open('../dump', 'r') as f:
    for line in f:
      dumps.append(line.strip())
  return dumps

def dumps_to_db():
  j = Jsondb()
  db = j.db

  print len(db)

  dumps = get_dumps()
  for line in dumps:
    try:
      d = get_domain_parts('http://' + line)
      u = urlparse('http://' + line)
      p = u.path
      url = '%s.%s' % (d.domain, d.tld)
      if url not in db:
        db[url] = {
          'subdomains': [],
          'paths':      []
        }
      if p not in db[url]['paths']:
        db[url]['paths'].append(p)
      if d.subdomains:
        for domain in d.subdomains:
          if domain not in db[url]['subdomains']:
            db[url]['subdomains'].append(domain)
    except ValueError:
      pass

  j.update(db)
  print len(j.db)
  #j._print()
  j.save()

def update_db():
  j = Jsondb(f='/home/johnny/dev/backzupz/spider/a/_dumps/db_15-05-26.json')
  db = j.db

  for line in db:
    try:
      d = get_domain_parts('http://' + line)
      db[line]['tld'] = d.tld
    except ValueError:
      print line

  j.update(db)
  j.save()

def domain_stats():
  j = Jsondb(f='/home/johnny/dev/backzupz/spider/a/_dumps/db_15-05-26.json')
  db = j.db

  stats = {}
  for line in db:
    tld = db[line]['tld']
    if tld in stats:
      stats[tld] += 1
    else:
      stats[tld] = 1

  return stats

def main():
  stats = domain_stats()
  sorted_x = sorted(stats.items(), key=operator.itemgetter(1))
  for x in sorted_x:
    print x

if __name__ == '__main__':
  #update_db()
  main()