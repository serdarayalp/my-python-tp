# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number.

'''
Syntax: 
  range(start, stop, step) 

Parameter 	Description
---------------------------------
start 	    Optional. An integer number specifying at which position to start. Default is 0
stop 	    Required. An integer number specifying at which position to stop (not included).
step 	    Optional. An integer number specifying the incrementation. Default is 1
'''

# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
r = range(6)
for i in r:
    print(i)

print("\n")

# Create a sequence of numbers from 3 to 5, and print each item in the sequence:
r = range(3, 6)
for i in r:
    print(i)
