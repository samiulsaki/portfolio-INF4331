#!/usr/bin/env python3
# Find script
'''
It would be fine if just root along with file name will be printed on the shell.abs
But that would print out only the given directory argument ar root folder instead of
its absolute path. For example if the arguments are as follows:

python find.py <file_extention> <file_location>
e.g.: python find.py .txt .

this will only print as such:

./filename1.txt
./filename2.txt
....

instead of 

absolute_path_of_file/filename1.txt
absolute_path_of_file/filename2.txt
....

To avoid this absoulte path of the files are printed along with the filenames.

'''

import os, sys

os.system('clear')

extension=sys.argv[1]
dir=sys.argv[2]

def recursive(dir):
  for root,folders,files in os.walk(dir):
    for file in files:
      if file.endswith(extension):
        print(os.path.abspath(root),file,sep="/")


recursive(dir)