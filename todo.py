#!/usr/bin/env python3

from sys import argv
import os
import todo_cfg

def write_txt(file, string):
    #Write one line to file with newline
    with open(file, 'a') as file:
        file.write(string + '\n')
                 
def read_all_lines(file):   
    #Reads all the lines from a file  
    if os.stat(file).st_size == 0:
        print('todo file is empty')
    with open(file, 'r') as file: 
        return file.readlines()

def read_line(file, line):
    #Reads one or more lines from a file
    with open(file, 'r') as file: 
        return file.readlines()[line - 1]

def remove_line(file, string):
    #Remove a line from a file
    all_txt = read_all_lines(file)
    #line_to_remove = read_line(file, string)
    with open(file, 'w') as file:
        for line in all_txt:
            if line != string:
                file.write(line)

#TODO -- do multiple items
#TODO -- print x of y listed
#TODO -- raise error when todo.txt is empty
#TODO -- do multiple dont shift the index until done.
#TODO -- accept d and do

#read text and remove line are good example of how to do architecturally
#read text

#need to parse out each argument so that you can add and remove in one line
# loop through each argument.
#arguments are already a list. Just need to separate by ""

#tp a thing to add, another thing, one more
#tp a work this way too, d 2

if __name__ == '__main__':
    #filepaths here
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    arguments = ' '.join(argv[1:]).split(', ')

    for arg in arguments:
        if len(argv) == 1: #argv 0 is the py file itself
            print("''man todopy' for usage'") 
        elif arg[0] == 'l' or arg[0] == 'ls':
            for i, line in enumerate(read_all_lines(todo_txt), 1):
                print(i, line.replace("\n", ""))       
        elif arg[0] == 'a' or arg[0] == 'add':
            write_txt(todo_txt, arg.split(' ', 1)[1])    
        elif arg[0] == 'd' or arg[0] == 'do':
            line = read_line(todo_txt, int(arg[1:].strip()))
            write_txt(done_txt, line.replace("\n", ""))
            remove_line(todo_txt, line) 