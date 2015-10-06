import json

class Jsondb:
  def __init__(self, f='db.json'):
    self.f  = f
    self.db = self.load()

  def load(self):
    with open(self.f, 'r') as _f:
      data = json.load(_f)
    return data

  def save(self):
    with open(self.f, 'w') as _f:
      data = json.dump(obj=self.db, fp=_f, indent=0)
    return data

  def update(self, db):
    self.db = db

  def _print(self):
    data = json.dumps(obj=self.db, indent=4)
    print data

  def add_key(self, key='lol'):
    for o in self.db:
      try:
        self.db[o][key] = ''
      except:
        pass

def test():
  j = Jsondb()
  db = j.db

  print len(db)

  #j.update(db)
  #print j.db
  #j.save()

if __name__ == '__main__':
  test()