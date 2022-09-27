#!/usr/bin/env python3

from sys import argv
from os import stat
from datetime import datetime
from typing import List, TextIO
import todo_cfg

#Maybe use this instead to refactor
#https://docs.python.org/3/library/argparse.html

def print_all_contexts(file: TextIO) -> None:
    '''prints all unique contexts - '@' - that I have in text file

    Args:
        file: the file to check
    Returns:
        None
    '''
    pass

def print_context(file: TextIO, context: str) -> None:
    '''prints all str lines with param context in them

    Args:
        file: The file to check
        context: The context to locate
    Returns:
        None
    '''
    all_lines = read_all_lines(file)
    for i, line in enumerate(all_lines, 1):
        if '@' in line:
            if context in line:
                print(line.replace('\n', ''))
                return
    print('No such context')

def print_tasks_shown(file: TextIO) -> None:
    ''' prints the # of tasks shown out of total tasks
    count context and total

    Args:
        file: The file to check
    Returns:
        None 
    '''
    pass

def alphabetize_file(file: TextIO) -> None:
    '''Alphabetizes the items in a text file.

    Args:   
        file: The file to alphabetize
    Returns:
        None 
    '''

def check_todos_done(file: TextIO) -> int:
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            pass
        return i

def file_is_empty(file: TextIO) -> bool:
    ''' Checks if a text file is empty

    Args:
        file: the file to check
    Returns:
        True if the file is empty. False if it is not empty 
    '''
    if stat(file).st_size == 0:
        return True
    return False

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
    with open(file, 'r') as f: 
        if file_is_empty(file):
            print('The file is empty.')
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

def remove_line(file: TextIO, line_list: List[str]) -> None:
    '''Removes entire line with exact matches of all str from list[str] in file

    Calls the read_all_lines method and stores all the lines in a variable 'all_txt'
    Opens the file in write mode and rewrites all of the strings to the file -- skips over str in line_list

    Args:
        file: The text file to remove a line from
        string: The string to remove from the file
    Returns:
        None
    '''
    all_txt = read_all_lines(file)
    with open(file, 'w') as f:
        for line in all_txt:
            if line not in line_list:
                f.write(line)

#TODO -- list out context
#TODO -- print x of y listed
#TODO -- d just 1 2 to do both
#TODO -- add do add what should happen
#TODO -- group all args togethor? 
#TODO -- make main as bare as possible

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
#group all adjacent dos togethor and make single method call to remove_lines

if __name__ == '__main__':    
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt
    lines_to_remove = []

    arguments = ' '.join(argv[1:]).split(', ')
    #print(f'arguments {arguments[0]}')

    for arg in arguments:
        if len(argv) == 1: #argv 0 is the py file itself
            print('add usage later')                       #TODO  
        elif arguments[0] == 'lsd':
            print(check_todos_done(done_txt))
        elif arg[0] == 'l' or arg[0] == 'ls':
            if '@' in arguments[0]:
                #print_context(todo_txt, arguments[0])
                arguments = str(arguments[0])
                arguments = arguments[arguments.index('@') : ]
                print_context(todo_txt, arguments)
                break
            for i, line in enumerate(read_all_lines(todo_txt), 1):
                print(i, line.replace('\n', ''))                  
        elif arg[0] == 'a' or arg[0] == 'add':
            write_txt(todo_txt, arg.split(' ', 1)[1])    
        elif arg[0] == 'd' or arg[0] == 'do':
            if file_is_empty(todo_txt):
                print('Todo file is empty -- you cannot do this task.') 
                raise SystemExit(1)
            line = read_line(todo_txt, int(arg.split(' ', 1)[1]))
            lines_to_remove.append(line)
            dt = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            write_txt(done_txt, line.replace('\n', ', ') + dt)
    if lines_to_remove:
        remove_line(todo_txt, lines_to_remove)
