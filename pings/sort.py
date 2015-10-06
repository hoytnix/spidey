from os       import path, stat, walk, system
from os.path  import join, getsize

# Crude.

class SortDumps:
  def __init__(self, engine='google'):
    self.engine  = engine
    self.engines = self.get_engines()
    self.files   = self.get_files()

  def mash(self):
    no = 0.0
    wins = []

    _files = []
    for _file in self.files:

      print _file
      break

      if _file[0] != '_' and _file != '0':
        print "un-<weblog %s" % _file
        #Remove <weblog lines
        system( "sed -i '/^<weblog/d' %s" %
          ('./dumps/%s/%s'  % (self.engine, _file))
        )
        if self.engine == 'weblogs':
          system( "sed -i '/^    <weblog/d' %s" %
            ('./dumps/%s/%s'  % (self.engine, _file))
          )          
        print "Dedupe %s" % _file
        #Remove duplicates
        system( "awk '!seen[$0]++' %s > %s" %
          (
            './dumps/%s/%s'  % (self.engine, _file),
            './dumps/%s/_%s'  % (self.engine, _file)
          )
        )

  def get_files(self):
    f = None
    for root, dirs, files in walk('./dumps/%s' % self.engine):
       f = files
    return f

  def get_engines(self):
    engines = []
    for root, dirs, files in walk('./dumps'):
      d = root
      d = d.replace('./dumps', '')
      d = d.replace('/',       '')
      if d == '':
        pass
      else:
        engines.append(d)
    return engines

def main():
  # Why is there multiple instances of the class?
  s = SortDumps()
  engines = s.engines
  for engine in engines:
    _s = SortDumps(engine=engine)
    print engine, len(_s.files)
    _s.mash()

if __name__ == '__main__':
  main()
