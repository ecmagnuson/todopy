#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_file(file, *args):
    with open(file, 'a') as file: #a instead of w is append :)
            file.write(' '.join(argv[2:])) 
            file.write('\n')                     #TODO make better new line

def read_file(file):                             #TODO get index to work
    with open(file, 'r') as file:
        print(file.read())                

if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage")
        raise SystemExit(0)

    if argv[1] == 'a' or argv[1] == 'add':
        write_file(todo_txt, argv[1:])
        
    if argv[1] == 'l' or argv[1] == 'ls':
        read_file(todo_txt)