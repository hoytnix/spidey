from urllib.parse import urlparse
import operator

from lists.tlds import cctlds, gtlds

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
    'info', 'biz', 'mobi',
    
    # ccTLD

    # UK
    'co.uk', 'org.uk', 'ac.uk', 'gov.uk', 'ltd.uk', 
    'me.uk', 'mod.uk', 'net.uk', 'nic.uk', 'nhs.uk',
    'soc.uk', 'cym.uk', 'scot.uk',
    # Canada
    'qc.ca', 'on.ca', 'bc.ca', 'mb.ca',
    # Australia
    'org.au', 'com.au', 'net.au', 'asn.au',
    # New Zealand
    'org.nz', 'net.nz', 'school.nz', 'ac.nz',
    # Japan
    'ed.jp', 'ac.jp', 'jp.net',
    # Poland
    'net.pl', 'org.pl', 'biz.pl',
    
    'org.il',
    'org.mx',
    'org.es',

]
for x in cctlds:
    _tlds.append(x)
for x in gtlds:
    _tlds.append(x)

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

def dumps_to_db(dumps):
    db = {}

    for line in dumps:
        try:
            d = get_domain_parts('http://' + line)
            u = urlparse('http://' + line)
            p = u.path
            url = '%s.%s' % (d.domain, d.tld)
            if url not in db:
                db[url] = {
                    'subdomains': [],
                    #'paths':      []
                }
            #if p not in db[url]['paths']:
            #  db[url]['paths'].append(p)
            if d.subdomains:
                for domain in d.subdomains:
                    if domain not in db[url]['subdomains']:
                        db[url]['subdomains'].append(domain)
        except ValueError:
            pass

    return db