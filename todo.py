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
        return file.readlines()

def read_line(file, line):
    '''Reads one or more lines from a file'''
    with open(file, 'r') as file: 
        return file.readlines()[line - 1]

def remove_line(file, string):
    '''Remove a line from a file'''
    all_txt = read_all_lines(file)
    line_to_remove = read_line(file, string)
    with open(file, 'w') as file:
        for line in all_txt:
            if line != line_to_remove:
                file.write(line)

#TODO -- write multiple items
#TODO -- do multiple items
#TODO -- print x of y listed
#TODO -- working with string 

if __name__ == '__main__':
    #filepaths here
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage") 
    elif argv[1] == 'l' or argv[1] == 'ls':
        for i, line in enumerate(read_all_lines(todo_txt), 1):
            print(i, line.replace("\n", ""))      
    elif argv[1] == 'a' or argv[1] == 'add':
        task = ' '.join(argv[2:])
        write_txt(todo_txt, task)    
    elif argv[1] == 'd' or argv[1] == 'do':
        line = read_line(todo_txt, int(argv[2]))
        write_txt(done_txt, line.replace("\n", ""))
        remove_line(todo_txt, int(argv[2]))