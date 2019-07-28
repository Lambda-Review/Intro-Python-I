"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys, os, platform
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("This is the name of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("This is the path of the script:", sys.path[0])
print("This is the path of python3.6 file:", sys.path[1])
print("This is the path of python3.6 install folder:", sys.path[2])
print("This is the Python Version I'm running:", sys.version)

# Print out the OS platform you're using:
# *  Platform or sys can be used for this. Also needs os,platform modules
# YOUR CODE HERE

print("This is the Operating System:", os.name)
print("This is the Operating System:", platform.system())
print("This is the Operating System:", sys.platform)


# Print out the version of Python you're using:
# YOUR CODE HERE
print("This is the Python Version I'm running:", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Current process ID:", os.getpid())
print("Current process ID:", os.getpgid(0))


# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("machine name:", os.uname())

