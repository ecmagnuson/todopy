#!/usr/bin/env python3

import sys
import todo_cfg

todo_txt = todo_cfg.todo_txt
done_txt = todo_cfg.done_txt

if len(sys.argv) == 1: #It's index 1 - so if no arg passed
    print("'man todopy' for usage")
    raise SystemExit(0)

#accept variable number of args

if sys.argv[1] == 'a' or sys.argv[1] == 'add':
    with open(todo_txt, 'a') as todo_txt: #a instead of w is append :)
        todo_txt.write('\n') #This seems really sloppy but its the only way I can find to do it right now
        todo_txt.write(' '.join(sys.argv[2:])) 

if sys.argv[1] == 'l' or sys.argv[1] == 'ls':
    with open(todo_txt, 'r') as todo_txt:
        lines = todo_txt.read()

    for line in lines:
        print(line, end = '') #Need to look at this later.
        

