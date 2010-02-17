#!/usr/bin/env python
#coding=utf-8

import os
import sys

""" converter for michael nock's netrunner deck database
    author: Valentin Haenel

"""

def convert(input_filename, output_filename):
    """ convert single file """
    f_in = file(input_filename, 'r')
    f_out = file(output_filename,'w')
    prefix = True
    for line in f_in.readlines():
        if line.startswith("Description"):
            prefix = True

        if prefix:
            f_out.write('#')
        f_out.write(line)

        if line.startswith("Deck list:"):
            prefix = False

    f_in.close()
    f_out.flush()
    f_out.close()

def convert_directory(directory):
    print "dir: ",directory
    for item in (os.path.join(directory,item) for item in os.listdir(directory)
            if not item.startswith('.')):
        if os.path.isdir(item):
            convert_directory(item)
        elif os.path.isfile(item):
            convert(item,item)


if __name__ == "__main__":
    convert_directory(sys.argv[1])

