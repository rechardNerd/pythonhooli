# =================================================================================
# Script Name     : logs.py
# Author          : Craig Richards
# Created         : 12th Dec 2021
# Last Modified   :
# Version         : 1.0
# Modifications   : 1.1 - Added the variable zip_program so
#                   you set it for the zip program on whchever OS, so to run on a
#                   different OS just change the locations of threse two variables.
# Description     : This script will search for all *.log files in given directory,
#                   zip them using the program you specify and then date stamp them
# =================================================================================

import os   # Load the library Module
from time import strftime   # Load just the strftime Module from Time

logsdir = "c:\puttylogs"    # Set the variable logsdir
zip_program = "zip.exe"     # Set the variable zip_program - 1.1

for files in os.listdir(logsdir):   # Find all the files in the directory
    if files.endswith(".log"):  # Check to ensure the files in the directory end in .log
        files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
        os.chdir(logsdir)   # Change the directory to the logsdir
        os.system(zip_program + "" + files1 + " " + files) # Zip the logs into dated zip files for each server. - 1.1
        os.remove(files)