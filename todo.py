#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_txt(file, *args):
    with open(file, 'a') as file: #a instead of w is append :)
        return file.write(' '.join(argv[2:]))                         #TODO new line
            
def read_txt(file):                                                  #TODO get index to work
    with open(file, 'r') as file:
        return file.readlines()

def remove_txt(file, line):
    print(line)
    lines = read_txt(file)
    print(lines[1])

    
    
    
if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage")
        raise SystemExit(0)
            
    if argv[1] == 'a' or argv[1] == 'add':
        print(write_txt(todo_txt, argv[1:]))
        
    if argv[1] == 'l' or argv[1] == 'ls':
        print(read_txt(todo_txt))

    if argv[1] == 'd' or argv[1] == 'do':
        remove_txt(todo_txt, argv[2])
