#!/usr/bin/env python3

from sys import argv
import os
from datetime import datetime
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

def read_line(file, line_num) -> str:
    #Reads one line from a file
    return read_all_lines(file)[line_num - 1]

def remove_line(file, string):
    #Remove a line from a file
    all_txt = read_all_lines(file)
    #line_to_remove = read_line(file, string)
    #keep track before removing
    with open(file, 'w') as file:
        for line in all_txt:
            if line != string:
                file.write(line)

def remove_lines(file, line_list):
    line_list = ['a', 'b']
    all_txt = read_all_lines(file)
    with open(file, 'w') as file:
        for line in all_txt:
            #if str in array then dont write the line
            #update this line to check for matches inside of line_list.  -- TODO
            if line != string:
                file.write(line)


#TODO -- combine the read methods
#TODO -- do multiple items
#TODO -- print x of y listed
#TODO -- raise error when todo.txt is empty
#TODO -- do multiple dont shift the index until done.
#TODO -- accept d and do
#TODO -- add date when done
#TODO -- d just 1 2 to do both
#TODO -- ls functionality
#TODO -- add do add what should happen

#read text and remove line are good example of how to do architecturally
#read text

#need to parse out each argument so that you can add and remove in one line
# loop through each argument.
#arguments are already a list. Just need to separate by ""

#tp a thing to add, another thing, one more
#tp a work this way too, d 2

#if no args match then print usage.
#doc strings for return value
#type hints
#list done on certain date. lsd
#

#group all adjacent dos togethor and make single method call to remove_lines


if __name__ == '__main__':    
    #filepaths here
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt
    dt = datetime.now().strftime('%m/%d/%Y %H:%M:%S')

    arguments = ' '.join(argv[1:]).split(', ')
    print(f'arguments {arguments}')

    for arg in arguments:
        if len(argv) == 1: #argv 0 is the py file itself
            print('add usage later')                       #TODO  
        elif arg[0] == 'l' or arg[0] == 'ls':
            for i, line in enumerate(read_all_lines(todo_txt), 1):
                print(i, line.replace('\n', ''))                  
        elif arg[0] == 'a' or arg[0] == 'add':
            write_txt(todo_txt, arg.split(' ', 1)[1])    
        elif arg[0] == 'd' or arg[0] == 'do':
            print(f'args {arg}')
            line = read_line(todo_txt, int(arg[1:].strip()))
            write_txt(done_txt, line.replace('\n', ', ') + dt)
            remove_line(todo_txt, line)