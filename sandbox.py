#!/usr/bin/env python3

def arguments(line, *args):
    print(len(args))
    print(args[0])

arguments('s', 'ssdf')