#!/bin/sh

#If this horribly pains you to put in Home then feel free to change it. 
#Be warned though, changing this rm -rf's your life...........
#I hope can feel comfortable being able to do things in your home :)

todo_dir=/home/"$USER"/.todopy

echo -n "Want me to pick the default location for the todopy directory (~/.todopy) [y/n]? "
read answer

if [ "$answer" != "${answer#[Yy]}" ] ; then 
    if [ -d "$todo_dir" ]
        then echo "You already have a .todo dir in Home! Either remove it or change path in setup.sh"
        echo "PS im located in ${PWD} :)"
    fi

    if [ ! -d "$todo_dir" ] 
        echo "I'm glad you feel comfortable being able to do things in your home"
        then mkdir "$todo_dir"
        touch ${todo_dir}/todo.txt ${todo_dir}/done.txt
    fi
fi

#todo_dir=$1

#todo_dir=/home/"$USER"/.todopy