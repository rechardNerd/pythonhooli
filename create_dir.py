"""
Code to directly use in file to
create directory in home location

Note:- I Have used python package so if you want
to create in the main directory of you project use
pardir + "\\" + name in functions

All the folder operations are done on home
project directory
"""
import os
from os import chdir
from os import makedirs
from os import removedirs
from os import rename
from os .path import exists
from os.path import pardir
from shutil import copytree
from shutil import move

# Create a directory
def create_directory(name):
    print(pardir)
    print(pardir + "\\" + name)
    if exists(pardir + "\\" + name):
        print('Folder already exists...Cannot Overwrite this')
    else:
        makedirs(pardir + "\\" + name)

# Rename a directory
def rename_directory(direct,name):
    rename(direct,name)

# Sets the working directory
def set_working_directory():
    chdir(pardir)

# Backup the folder tree
def backup_files(name_dir,folder):
    copytree(pardir,name_dir + ':\\' + folder)

# move folder to specific location
# Overwrites the file if it already exists
def move_folder(filename,name_dir,folder):
    if not exists(name_dir + ":\\" + folder):
        makedirs(name_dir + ":\\" + folder)
    move(filename,name_dir + ":\\" + folder +"\\" )

"""
For test purpose:
    1.create_directory("test")
    2.rename_directory("test","demo")
    3.delete_directory("demo")
    4.backup_files('D','buckup_project')
    5.move_folder(pardir + '\\' + 'test.txt','D','name')
"""

def main():
    create_directory("test")
    rename_directory("test","demo")


if __name__ == '__main__':
    main()