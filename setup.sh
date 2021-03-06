#!/bin/sh

todo_dir=/home/"$USER"/.todopy
todo_tests=/home/"$USER"/.todopy/tests

echo -n "Want me to pick the default location for the todopy directory (~/.todopy) [y/n]? "
read answer

#I have no idea why.. but != y means when I type y the nested if executes..
if [ "$answer" != "${answer#[Yy]}" ] ; then 
    #This if is clunky but for now I want to work on the actual py program.
    if [ -d "$todo_dir" ]
        then echo "You already have a .todo dir in Home! Either remove it or change path in setup.sh"
        echo "PS im located in ${PWD} :)"
    fi

    if [ ! -d "$todo_dir" ] 
        echo "I'm glad you feel comfortable being able to do things in your home"
        then mkdir "$todo_dir"
        touch ${todo_dir}/todo.txt ${todo_dir}/done.txt
        touch ${todo_tests}/todo_test.txt ${todo_tests}/done_test.txt
        echo "task, date" >> ${todo_dir}/done.txt
    fi
fi

#This is pretty lame but I want to work on the todo.py file
if [ "$answer" != "${answer#[Nn]}" ] ; then 
    echo "You can choose your default directory in the setup.sh script."
fi

#eventually populate the todo.cfg file with the directories
#make a man page and then move the man page to where it should go.