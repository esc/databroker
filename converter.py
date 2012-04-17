#!/usr/bin/env python
#coding=utf-8

import os
import sys

""" converter for michael nock's netrunner deck database
    author: esc

"""

def convert(filename):
    """ convert single file by overwrite"""
    f = file(filename, 'r')
    lines = f.readlines()
    f.close()
    prefix = True
    f = file(filename, 'w')
    for line in lines:
        if line.startswith("Description"):
            prefix = True
        if prefix:
            f.write('#')
        f.write(line)
        if line.startswith("Deck list:"):
            prefix = False

    f.flush()
    f.close()

def convert_directory(directory):
    """ convert directory recursively """
    for item in (os.path.join(directory,item) for item in os.listdir(directory)
            if not item.startswith('.')):
        if os.path.isdir(item):
            convert_directory(item)
        elif os.path.isfile(item):
            print 'convert: ', item
            convert(item)


if __name__ == "__main__":
    convert_directory(sys.argv[1])

