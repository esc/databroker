#!/usr/bin/env python
#coding=utf-8

import os
import sys

""" converter for michael nock's netrunner deck database
    author: Valentin Haenel

"""

def convert(input_filename, output_filename):
    """ converter for michael nock's netrunner deck database """
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

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])

