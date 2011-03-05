#!/usr/bin/env python
#coding=utf-8

id =        "id"
set =       "set"
copyright = "copyright"
name =      "name"
type =      "type"
cost =      "cost"
rarity =    "ruling"
text =      "text"
ruling =    "ruling"
flavor =    "flavor"
artist =    "artist"


class card(dict):
    pass

class mws_parser():

    def __init__(self):
        self.cardlist = []

    def parse_mws(self,filename):
        file = open(filename)
        self.set = self._parse_single(file,name)
        while True :
            id_val = self._parse_single(file,id)
            if id_val == "" :
                return self.cardlist

            c = card()
            c[id] = id_val
            c[set] = self.set
            c[copyright] = self._parse_single(file,copyright)
            c[name] = self._parse_single(file,name)
            c[type] = self._parse_single(file,type)
            self.cardlist.append(c)

    def _parse_single(self, file, string):
        while True :
            l = file.readline()
            if l == "" :
                return ""

            if string+"=" in l:
                start = l.find(string)+len(string)+2
                end = l.find('"',start)
                return l[start:end]
        
if __name__ == '__main__':
    p = mws_parser()
    cardlist = p.parse_mws('Proteus.set')
    print cardlist
