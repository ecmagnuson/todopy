#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_txt(file, *args):
    with open(file, 'a') as file: #a instead of w is append :)
        return file.write(' '.join(argv[2:]))                         #TODO new line
            
def read_txt(file):                                                  #TODO get index to work
    with open(file, 'r') as file:
        return file.readlines()

    
if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage")
            
    elif argv[1] == 'a' or argv[1] == 'add':
        print(write_txt(todo_txt, argv[1:]))
        
    elif argv[1] == 'l' or argv[1] == 'ls':
        print(read_txt(todo_txt))

    else:
        print("'man todopy' for usage")