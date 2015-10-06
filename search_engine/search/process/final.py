from jsondb import Jsondb as DB

def get_contact_domains():
  db = DB(f='./json/01.json')
  json = db.db

  domains = []
  for key in json:
    domains.append(key)
  return domains

def get_word_domains():
  db = DB(f='./json/03.json')
  json = db.db

  domains = json['domains']
  return domains

def get_both(wd, cd):
  both = []
  i = 0
  for domain in wd:
    if domain in cd:
      both.append(domain)
    i+=1
    if i % 1000 == 0:
      print i

  return both

def main():
  word_domains    = get_word_domains()
  contact_domains = get_contact_domains()
  
  wd = word_domains
  cd = contact_domains

  both = get_both( wd = wd, cd = cd )
  print len(both)

  print '-' * 100

  for d in both:
    print d

if __name__ == '__main__':
  main()