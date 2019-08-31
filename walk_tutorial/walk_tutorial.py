import os

for dirpath, dirnames, files in os.walk('my_directory'):
    for filename in files:
        print(os.getcwd(), dirpath , filename)
