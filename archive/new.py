# Importing the os library
import os
 
# The path for listing items
path = '.'
 
# List of only files
files = [f for f in os.listdir(path) if os.path.isfile(f)]
 
# Loop to print each filename separately
for filename in files:
    print(filename)