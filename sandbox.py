#!/usr/bin/env python3

from sys import argv

def remove_txt(file, line):
    with open(file, 'r+') as file:
        file.seek(line)
        file.write('') #write over and remove
        file.truncate()

remove_txt('file.txt', 1)

