# 4. Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 


# 5. Label the program written in problem 4 with comment

import os

# Specify the directory path (you can change this to any path you want)
directory_path = '/'  # Current directory

try:
    # Get list of directory contents
    contents = os.listdir(directory_path)

    # Print each item in the directory
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")



# AI used