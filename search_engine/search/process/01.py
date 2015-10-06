from jsondb import Jsondb as DB

def get_archive():
  archive = []
  with open('../dumps/01', 'r') as f:
    for line in f:
      archive.append(line)
  return archive

def main():
  # Init DB
  db = DB(f = './json/01.json')
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
    
    if len(s) > 2:
      
      url = s[0].replace('file: ', '')

      i = 2
      while i < len(s):
        row = s[i]
        
        f = None; m = None
        if len(row) > 0:
          if row[0] == 'f':
            _f = row[13:]
            if 'fbml' not in _f and '.php' not in _f and 'oauth' not in _f:
              if 'facebook.com' in _f:
                if _f != 'facebook.com' and _f != 'facebook.com/':
                  f = _f
          if row[0] == 'm':
            _m = row[8:]
            if '@' in _m:
              m = _m

        if f or m:
          json[url] = {}
          if f:
            json[url]['facebook'] = f
          if m:
            json[url]['email'] = m

        i += 1

  #print json

  # Update DB
  db.update(json)
  db.save()

if __name__ == '__main__':
  main()