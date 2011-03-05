import os
import re
import sys
from xml.etree import ElementTree as xet

def extract_names(filename):
    return [c.attrib['name'] for c in
            xet.parse(filename).getroot().getchildren()[0].getchildren()]

def extract_all():
    data_path = "gccg_data"
    names = []
    for f in os.listdir(data_path):
        names += extract_names(os.path.join(data_path, f))
    return names

def read_file(filename):
    with open(filename) as f:
        lines = []
        for line in f.readlines():
            if not line.startswith('#'):
                ma = re.match('^[0-9]* (.*)', line.strip())
                if ma is not None:
                    lines.append(ma.groups()[0])
    return lines

def check_file(data_base, filename):
    unknown = []
    for card in read_file(filename):
        if card not in data_base:
            unknown.append(card)
    if unknown:
        print "WARNING: file %s contains unknown cards:" % filename
        print unknown

if __name__ == '__main__':
    data_base = extract_all()
    for filename in sys.argv[1:]:
        check_file(data_base, filename)
