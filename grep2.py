import re
import sys
import argparse
import glob
import os

"""
Grep program. Uses arg parser for robust argument parsing. Implements x and v flags, as well as multiple files.
#Alex Ashkeboussi
"""

# Obtains arguments arguments
parser = argparse.ArgumentParser()
parser.add_argument("regex", help="Regular expression to be searched for")
parser.add_argument("filenames", help="Files that will be searched for regular expression", nargs="+")
# Optional Arguments
parser.add_argument("--x", help="Select only those matches that exactly match the whole line.", action='store_true')
parser.add_argument("--v", help="Invert the sense of matching, to select non-matching lines.", action='store_true')  

# pulls arguments from argparser
args = parser.parse_args()

# CLI flags
x = args.x
v = args.v

#Gets regex
regex = args.regex

#Gets files to search
filenames = args.filenames

#EXPERIMENTAL FILE aquisition- use regex...
#print glob.glob(os.path.abspath(__file__).replace("\\",""))
#print os.listdir(os.path.abspath(__file__).replace("\\\\","\\"))
#sys.exit(0)

# Parses each line 
for filename in filenames:#Each iteration opens up a new file as specified in the command line arguments and executes next loop
    
    # Attempts to open file
    try:
        currentFile = open(filename)
    except IOError:
        print "Error -- file " + filename + " not found"
        continue
    
    # Pulls first line    
    currentline = currentFile.readline()
    
    # Displays filename if there is more than one
    if len(filenames) > 1:
        print "\n<Found in " + filename + ">"
    
    # Each iteration checks for an exact match or a partial match (depending on arguments) and prints the line in the case of a match    
    while currentline:
        # Does a search match
        if x == 0:
            if re.search(regex, currentline):
                if v == 0:
                    print currentline
            elif v == 1:
                print currentline
            
        # Does an exact match search
        elif x == 1:
            if (re.match(regex, currentline)) and (len(currentline.replace("\n", "")) == len(regex)):
                if v == 0:
                    print currentline
                elif v == 1:
                    print currentline
        
        # Pulls next line    
        currentline = currentFile.readline()
    
    # Closes file
    currentFile.close()