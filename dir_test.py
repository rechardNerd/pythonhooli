# Script Name       :   dir_test.py
# Author            :   Craig Richards
# Created           :   8th December 2021
# Last Modified     :   by- Joshua Covinfton 05 October 2021
# Version           :   1.0
# Description       :   Tests to see if the directory testdir exists,
#                       if not it will create directory for you
from __future__ import print_function

import os

def main():
    CheckDir = input("Enter the name of the directory to check: ")
    print()

    if os.path.exists(CheckDir): # Check if the dir exists
        print("The directory exists")
    else:
        print("No directory found for " + CheckDir) # Output if no directory
        print()
        option = input("Would you like this directory create? y/n: ")
        if option == "n":
            print("Goodbye")
            exit()
        if option == 'y':
            os.makedirs(CheckDir) # Create a new dir for the given name
            print("Directory create for " + CheckDir)
        else:
            print("Not an option. Exiting")
            exit()

if __name__ == '__main__':
    main()
