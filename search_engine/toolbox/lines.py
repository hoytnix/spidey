#!/usr/bin/env python

'''
py3k: True
'''

class Lines:
    def __init__(self, f):
        self.path = f
        self.d = []
        self.compile()

    def compile(self):
        offset = 0
        with open(self.path, 'r') as f:
            for line in f:
                self.d.append(offset)
                offset += bytes(line, 'utf-8').__len__()

    def find_line(self, n):
        offset = self.d[n]

        line = ''
        with open(self.path, 'r') as f:
            f.seek(offset)
            line = f.readline().strip()
        return line

def main():
    l = Lines(f='/opt/datas/yum')
    x = l.d.__len__()
    for n in range(x - 10, x):
        try:
            print( n, end=' ') 
            print( l.find_line(n=n) )
        except:
            pass

if __name__ == '__main__':
    main()