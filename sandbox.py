#!/usr/bin/env python3

#read things between commas basically. 
#but what if no commas?

#parse arguments between commas basically as one and then loop through. 
#if no commas then one argument



from sys import argv

arguments = ' '.join(argv[2:]).split(', ')

print(f'my arguments not split: {arguments}')

for arg in arguments:
    print(arg)