#!/usr/bin/env python3

from sys import argv

#print(*argv[1:])

def write(*args):
    print(*args)

write(argv[1:])