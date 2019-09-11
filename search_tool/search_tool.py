import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--search_string',
    '-s',
    default='',
    help='Search string to be searched')

parser.add_argument(
    '--folder',
    '-f',
    default='D:\folder',
    help='Folder to be searched for')

parser.add_argument(
    '-e',
    '--file_extension',
    nargs='+',
    default=['.cpp', '.h'],
    help='File extension for which search is to be made. By default it is _AppEventLog.txt')

input_arguments = parser.parse_args()

file_extensions = tuple([x.lower() for x in input_arguments.file_extension])
    
def search_files(directory='.'):
    
    for dirpath, dirnames, files in os.walk(directory):
               
        for name in files:
            
            if name.lower().endswith(file_extensions) :

                file_to_be_searched = os.path.join(dirpath, name)                
            
                with open(file_to_be_searched, errors='ignore') as current_file:
                    for line_no, line in enumerate(current_file, 1):
                        if input_arguments.search_string.lower() in line.lower():
                            print(file_to_be_searched, '(', line_no, ') :  ', line.strip())                


print('\n ############ Searching in path ', input_arguments.folder.strip())
search_files(input_arguments.folder.strip())
