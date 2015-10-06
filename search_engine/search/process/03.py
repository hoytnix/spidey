from jsondb import Jsondb as DB

def get_archive():
  archive = []
  with open('../dumps/03', 'r') as f:
    for line in f:
      archive.append(line)
  return archive

def main():
  # Init DB
  db = DB(f = './json/03.json')
  json = db.db
  print db.f, len(db.db)

  # Shortcuts :)
  br_1 = '-' * 100
  br_2 = '-' * 80

  # Get Archive!
  archive = ''.join(get_archive())
  
  # Process
  archive = archive.split(br_1)

  keywords = archive[0]
  archive  = archive[1]

  sites = archive.split(br_2)
  sites = sites[:-1]
  
  for site in sites:
    s = site.split('\n')

    for x in s:
      if x == '':
        s.remove('')
    
    if len(s) > 1:
      domain = s[0].replace('file: ', '')

      words = []
      i = 1
      while i < len(s):
        words.append(s[i])
        i += 1

      if domain not in json['domains']:
        json['domains'][domain] = [word for word in words]
      else:
        for word in words:
          json['domains'][domain].append(word)

      for word in words:
        if word not in json['words']:
          json['words'][word] = 1
        else:
          json['words'][word] += 1

  # Update DB
  db.update(json)
  db.save()

if __name__ == '__main__':
  main()