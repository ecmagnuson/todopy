#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_txt(file, string):
    '''Write one line to file with newline.'''
    with open(file, 'a') as file:
        file.write(string + '\n')
                 
def read_all_lines(file):   
    '''Reads all the lines from a file'''  
    with open(file, 'r') as file: 
            for i, line in enumerate(file.readlines(), 1):
                print(i, line, end = '') #TODO fix the end = ''

def read_line(file, line):
    '''Reads one or more lines from a file'''
    with open(file, 'r') as file: 
        return file.readlines()[line - 1].replace("\n", "")



def remove_line(file, line_num):
    line = read_all_lines(file, line_num)
    return line


if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage") 
    elif argv[1] == 'l' or argv[1] == 'ls':
        read_all_lines(todo_txt)   
    elif argv[1] == 'a' or argv[1] == 'add':
        task = ' '.join(argv[2:])
        write_txt(todo_txt, task)    
    elif argv[1] == 'd' or argv[1] == 'do':
        line = read_line(todo_txt, int(argv[2]))
        write_txt(done_txt, line)