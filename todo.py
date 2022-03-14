#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_str(file, string):
    with open(file, 'a') as file:
        file.write(string + '\n')

def write_txt(file, *args):
    with open(file, 'a') as file:
        file.write(' '.join(argv[2:]) + '\n')  
                      
def read_txt(file):           
    with open(file, 'r') as file: 
        for i, line in enumerate(file.readlines(), 1):
            print(i, line, end = '') #TODO fix the end = ''

def read_line(file, line_num):
    with open(file, 'r') as file:
        return file.readlines()[line_num - 1]

if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'mansss todopy' for usage")        
    elif argv[1] == 'a' or argv[1] == 'add':
        write_txt(todo_txt, argv[1:])    
    elif argv[1] == 'l' or argv[1] == 'ls':
        read_txt(todo_txt)
    elif argv[1] == 'd' or argv[1] == 'do':
        line = read_line(todo_txt, int(argv[2]))
        print(line)
        write_str(done_txt, line)