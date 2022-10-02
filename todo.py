#!/usr/bin/env python3

import sys
import os.path
from typing import List, TextIO
from datetime import datetime

HOME = os.path.expanduser('~')
TODODIR = os.path.join(HOME, '.todo')
TODOFILE = os.path.join(TODODIR, 'todo.txt')
DONEFILE = os.path.join(TODODIR, 'done.txt')

def help():
	print('a or add to add to the text file.')
	print('d or do to do a task.')
	print('l or ls to list out all of the tasks in the todo.txt file.')
	print('lsd or lsdone to list out what is done in the done.txt file.')

def setup():
	''' set up the text file database for first use
	if todofile does not exist,
	create it with a blank line at the top for the 'done' function to use '''

	if not os.path.exists(TODODIR):
		os.makedirs(TODODIR)
	with open(TODOFILE, 'w') as todo:
		todo.write('\n')
	with open(DONEFILE, 'w') as done:
		pass

def add(args: List[str]):
	if len(args) > 0:
		# take a single argument from the shell
		with open(TODOFILE, 'a') as todo:
			todo.write(' '.join(args))
			todo.write('\n')
	else:
		# take multiple args from std input, one per line
		while True:
			next = input('> ').strip()
			if next == '': break
			args.append(next)
		with open(TODOFILE, 'a') as todo:
			for arg in args:
				todo.write(arg)
				todo.write('\n')

def has_one_of(search_terms: List[str], word_list: List[str]):
	for word in word_list:
		if word in search_terms:
			return True
	return False

def ls(context: List[str]):
	if len(context) == 0:
		# No context
		with open(TODOFILE, 'r') as todo:
			for i, line in enumerate(todo.readlines()):
				if line.strip(' \r\n') == '':
					continue # ignore empty (deleted) lines
				print(f'({i})', line, end='')
	else:
		# With 1 or more contexts
		with open(TODOFILE, 'r') as todo:
			for i, line in enumerate(todo.readlines()):
				if line.strip(' \r\n') == '':
					continue # ignore empty (deleted) lines
				#if this line's context is in this line of the todo
				if (has_one_of(context, line.split())):
					print(f'({i})', line, end='')

def ls2(context: List[str]):
	with open(TODOFILE, 'r') as todo:
		for i, line in enumerate(todo.readlines()):
			if line.strip(' \r\n') == '':
				continue # ignore empty (deleted) lines
			#if this line's context is in this line of the todo
			# or, if there's no context we print out everything
			if (len(context) == 0 or has_one_of(context, line.split())):
				print(i, line, end='')

def get_context(line_num: List[int]):
	'''get context of a line in file '''
	#open the file. Find the line. Read the context
	todo_lines = []
	with open(TODOFILE, 'r') as todo:
		todo_lines = todo.readlines()
		line_w_context = todo_lines[line_num[0]]
		context = line_w_context[line_w_context.index('@') : ]
	return context.strip(' \r\n')

def ls_contexts():
	contexts = []
	with open(TODOFILE, 'r') as todo:
		for line in todo.readlines():
			if line.strip(' \r\n') == '':
				continue # ignore empty (deleted) lines
			if not line[line.index('@') + 1 :].strip() in contexts:
				contexts.append(line[line.index('@') + 1 :].strip())
	print(sorted(contexts))

def validate_contexts(contexts: List[str]):
	pass

def to_ids(str_ids: List[str]):
	return [int(id) for id in str_ids]

def now_date():
	return datetime.now().strftime(', %m/%d/%Y %H:%M:%S')

def done(ids: List[int]):
	todos = []
	with open(TODOFILE, 'r') as todo:
		todos = todo.readlines()
	done = []
	now = now_date()
	for i, line in enumerate(todos):
		line = line.strip(' \r\n')
		if (i in ids and line != ''):
			done.append(f'({i}) {line} {now}')
			# first line is empty, copy this to clear this line
			todos[i] = todos[0]
	# replace the todo file with the new contents
	with open(TODOFILE, 'w') as todo:
		for todo_line in todos:
			todo.write(todo_line)
	# append the 'done' items to the done file
	with open(DONEFILE, 'a') as done_file:
		for done_item in done:
			done_file.write(done_item)
			done_file.write('\n')
	# TODO (in the code): give an error when an id is invalid (already doned or past the end of the file or negative)

def lsdone():
	with open(DONEFILE, 'r') as done:
		for i, line in enumerate(done.readlines()):
			print(line, end='')

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('No commands found..')
		sys.exit(1)
	if not os.path.exists(TODOFILE):
		setup()
		
	cmd = sys.argv[1]
	#print(cmd) debugging

	if cmd == 'ls' or cmd == 'l':
		contexts = sys.argv[2:]
		validate_contexts(contexts)
		ls(contexts)
	elif cmd == 'lsc':
		ls_contexts()
	elif cmd == 'add' or cmd == 'a':
		add(sys.argv[2:])
	elif cmd == 'do' or cmd == 'd':
		ids = to_ids(sys.argv[2:]) #list of the id.
		done_context = [(get_context(ids))] #get the context from the id
		print(done_context)
		done(ids) #do it
		ls(done_context) #print out the context BUG here
	elif cmd == 'lsdone' or cmd == 'lsd':
		lsdone()
	elif cmd == 'reset':
		setup()
	elif cmd == 'help':
		help()
	else:
		print('Command not found..')
		print('Use help argument for availible commands')
		sys.exit(1)