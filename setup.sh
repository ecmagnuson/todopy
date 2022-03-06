#!/bin/sh

#If this horribly pains you to put in Home then feel free to change it. 
#Be warned though, changing this rm -rf's your life...........
#I hope can feel comfortable being able to do things in your home :)

echo "do you want to make the todopy directory in the default path: ~/.todopy? [y/n]"


#todo_dir=$1

#todo_dir=/home/"$USER"/.todopy

if [ -d "$todo_dir" ]
then echo "You already have a .todo dir in Home! Either remove it or change path in setup.sh"
    echo "PS im located in ${PWD} :)"
fi

if [ ! -d "$todo_dir" ]
then mkdir "$todo_dir"
     touch ${todo_dir}/todo.txt ${todo_dir}/done.txt
fi