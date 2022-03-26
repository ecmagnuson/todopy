run the setup.sh script.
It will create a '.todopy' directory in your home directory.
inside of '.todopy' it will populate two text files: todo.txt and done.txt
the todopy_dir will be exported to a todopy.cfg 
Python will read in from the todopy.cfg for the filepaths. 

This was inspired by the todo.txt cli written in shell.
I decided to make my own to learn and fix some annoyances that were bothering me

The base functionality is complete, albiet extremly messy and hacky in so many ways - which I will fix when I have the time.

Functionality:
1. list everything from the text file
2. list only specific contexts from the text file
3. list all present contexts in a file
4. Add things to do to text file, with multile add functionality
5. remove things from the file, with multiple do functionality
6. When something is done, it removes it from todo.txt and adds it to done.txt with date timestamp
7. Can add and remove with one line
8. Shows the items in order they were added
9. Count the amount of tasks I've completed - for fun :D
