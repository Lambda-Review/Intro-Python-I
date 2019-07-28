"""
Python is a strongly-typed language under the hood, which means 
that the types of values matter, especially when we're trying
to perform operations on them. 

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
y_intz = int(y)
print(y_intz + x)


# Write a print statement that combines x + y into the string value 57
# YOUR CODE HERE
x_string = str(x)
print(x_string + y)

# Others

s = "geeks"

# * Convert To a Tuple
c = tuple(s) 
print ("After converting string to tuple : ",end="") 
print (c) 

# * Printing string converting to set 
c = set(s) 
print ("After converting string to set : ",end="") 
print (c) 
