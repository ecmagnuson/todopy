#!/usr/bin/env python3

import sys
import todo_cfg

todo_txt = todo_cfg.todo_txt
done_txt = todo_cfg.done_txt

words = sys.argv[1]

#accept variable number of args
with open(todo_txt, 'a') as todo: #a instead of w is append :)
    todo.write(words)