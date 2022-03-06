#!/bin/sh

#If this horribly pains you to put in Home then feel free to change it. 
#Be warned though, changing this rm -rf's your life...........
#I hope you feel comfortable being able to do things in your own home :)
directory=~/.todo

if [ -d "$directory" ]
then echo "You already have a .todo dir in Home! Either remove it or change path in setup.sh"
    echo "PS im located in ${PWD} :)"
fi

if [ ! -d "$directory" ]
then mkdir "$directory"
fi

export directory