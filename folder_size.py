# ============================================================================
# Script Name       :   folder_size.py
# Author            :   Craig Richards
# Created           :   11th December 2021
# Last Modified     :   11th December 2021

# Modifications     :   Modified the printing method and added a few comments

# Description       :   This will scan the current directory and all subdirectors and display the size.

# ============================================================================
import os
import sys  # Load the library module and the sys moudle for  the argument vector

try:
    directory = sys.argv[1] # Set the variable directory to be the argument supplied by user.
    print(directory)
except IndexError:
    sys.exit("Must provide an argument.")

dir_size = 0    # Set the size to 0
fsizedicr = {
    'Bytes': 1,
    'Kilobytes': float(1) / 1024,
    'Megabytes': float(1) / (1024 * 1024),
    'Gigabytes': float(1) / (1024 * 1024 * 1024)
}

# Walk through all the directories. For each iteration,
#os.walk returns the folders,subfolders and files in the dir.
for (path, dirs, files) in os.walk(directory):
    for file in files:  # Get all the files
        filename = os.path.join(path,file)
        # Add the size of each file in the root dir to get the total size.
        dir_size += os.path.getsize(filename)

# List of units
fsizeList = [str(round(fsizedicr[key] * dir_size,2)) + "" + key for key in fsizedicr]
if dir_size == 0:
    # Sanity check to eliminate corner-case of empty
    print("File Enpty")
else:
    for units in sorted(fsizeList)[::-1]:   #Reverse sort list of units so smallest magnitude units print first.
        print("Folder Size: " + units)
