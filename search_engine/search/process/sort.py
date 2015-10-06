from jsondb import Jsondb as DB
import operator

def main():
  db = DB(f='03.json')
  json = db.db

  words = json['words']

  sorted_x = sorted(words.items(), key=operator.itemgetter(1))
  for x in sorted_x:
    print x

if __name__ == '__main__':
  main()