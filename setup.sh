#!/bin/sh

#If this horribly pains you to put in Home then feel free to change it. 
#Be warned though, changing this rm -rf's your life...........
#I hope you feel comfortable being able to do things in your own home :)
todopy_dir=~/.todo

if [ -d "$todopy_dir" ]
then echo "You already have a .todo dir in Home! Either remove it or change path in setup.sh"
    echo "PS im located in ${PWD} :)"
fi

if [ ! -d "$todopy_dir" ]
then mkdir "$todopy_dir"
fi