import os
from xml.etree import ElementTree as xet

def extract_names(filename):
    return [c.attrib['name'] for c in
            xet.parse(filename).getroot().getchildren()[0].getchildren()]

if __name__ == '__main__':
    data_path = "gccg_data"
    names = []
    for f in os.listdir(data_path):
        names.append(extract_names(os.path.join(data_path, f)))
    print names
