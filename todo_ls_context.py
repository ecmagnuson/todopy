#!/usr/bin/env python3

import todo_cfg

#Read a txt file and list the string after the @sign
#Only list unique values after the @sign
# '@work' is treated the same as '@     work' ..etc.

#can I do this without making a list?
context_lst = []

#filepath = '/home/elliott/Documents/todo/todo.txt'

todo_txt = todo_cfg.todo_txt
done_txt = todo_cfg.done_txt

filepath = todo_txt


with open(filepath) as txtfile:
    lines = txtfile.readlines()

for line in lines: # --> for each line in all of the lines filled out
    #swap the project after the context.
    #if they type 'do thing +project @context swap to @context +project
    try:
        
        if not '+' in line or line.index('+') > line.index('@'):
                       
            context = line[line.index('@') : ].strip() #--> context = '@work' or '@ work'.. etc.
            context = "".join(context.split())  # --> merges the two above to just context = '@work'
        
            if context not in context_lst:
                context_lst.append(context) 
                print(context)
            
        #if the index of + is < index of @ then swap them
        if line.index('+') < line.index('@'):
            project = line[line.index('+') : line.index('@')] # --> context = +project @context 
            line = line.replace(project, '')
            line = line[line.index('@') : ].strip()
            line = "".join(line.split())
            line = line + project

            if line not in context_lst:
                context_lst.append(line)
                print(line)

    except ValueError as e:
        pass
