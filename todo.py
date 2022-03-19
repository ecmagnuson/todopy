#!/usr/bin/env python3

from sys import argv
from os import stat
from datetime import datetime
from typing import List, TextIO
import todo_cfg

def write_txt(file: TextIO, string: str) -> None:
    '''Writes a string to a text file, leaves a new line

    Args:
        file: the file to write to
        string: the str to add to the file
    Returns:
        None
    '''
    with open(file, 'a') as f:
        f.write(string + '\n')
                 
def read_all_lines(file: TextIO) -> List[str]:   
    ''' Returns a str list of all the lines from a file. 

    Args:
        file: the text file to read from.
    Returns:
        A str list of all of the lines
    '''
    if stat(file).st_size == 0:
        print('todo file is empty')
    with open(file, 'r') as f: 
        return f.readlines()

def read_line(file: TextIO, line_num: int) -> str:
    '''Returns the string on one line of a file. 

    Args:
        file: the text file to read from
        line_num: the line number to read from. File starts at index 1
    Returns:
        the string at the specific line number of the text file
    '''
    return read_all_lines(file)[line_num - 1]

def remove_line(file: TextIO, string: str) -> None:
    '''Removes all instances of a string line from a file

    Calls the read_all_lines method and stores all the lines in a variable 'all_txt'
    Opens the file in write mode and rewrites all of the strings to the file -- except the line to remove

    Args:
        file: The text file to remove a line from
        string: The string to remove from the file
    Returns:
        None
    '''
    all_txt = read_all_lines(file)
    with open(file, 'w') as f:
        for line in all_txt:
            if line != string:
                f.write(line)




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
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

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
            line = read_line(todo_txt, int(arg[1:].strip()))
            dt = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            write_txt(done_txt, line.replace('\n', ', ') + dt)
            remove_line(todo_txt, line)