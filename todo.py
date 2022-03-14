#!/usr/bin/env python3

from sys import argv
import todo_cfg

def write_txt(file, string):
    '''Write text to file with newline.'''
    with open(file, 'a') as file:
        file.write(string + '\n')
                 
def read_txt(file, *args):   
    ''' This function will read text from a text file. If there are no args
    passed into the function it will print all the contents of the file.
    If there is an argument passed in it will return only the str on the
    row passed into the function. Starting at index 1.
    '''        
    with open(file, 'r') as file: 
        if len(args) == 0: 
            for i, line in enumerate(file.readlines(), 1):
                print(i, line, end = '') #TODO fix the end = ''
            return #better way to do this?
        return file.readlines()[args[0] - 1].replace("\n", "") #TODO fix this ugliness. 
        #I need to make a \n for writing to file, but i have to 
        # manually remove here to transfer it to done.txt, which is clunky.

def truncate_txt(file):
    return

def remove_line(file, line_num):
    line = read_txt(file, line_num)
    return line

#t do multiple at a time.

if __name__ == '__main__':
    todo_txt = todo_cfg.todo_txt
    done_txt = todo_cfg.done_txt

    if len(argv) == 1: #argv 0 is the py file itself
        print("'man todopy' for usage")        
    elif argv[1] == 'a' or argv[1] == 'add':
        task = ' '.join(argv[2:])
        write_txt(todo_txt, task)    
    elif argv[1] == 'l' or argv[1] == 'ls':
        read_txt(todo_txt)
    elif argv[1] == 'd' or argv[1] == 'do':
        line = read_txt(todo_txt, int(argv[2]))
        print(line)
        write_txt(done_txt, line)