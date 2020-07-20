counter = 100          # An integer assignment
miles = 1000.0       # A floating point
name = "John"       # A string

print(counter)

a = b = c = 1
print(a)

a, b, c = 1, 2, "john"

'''
Standard Data Types: Python has five standard data types:
    * Numbers
    * String
    * List
    * Tuple
    * Dictionary
'''

'''
Python supports four different numerical types:
    * int
    * long: Python allows you to use a lowercase l with long, but it is recommended that you use only an
        uppercase L to avoid confusion with the number 1. Python displays long integers with an uppercase L.
    * float
    * complex (complex numbers): A complex number consists of an ordered pair of real floating-point numbers
        denoted by x + yj, where x and y are the real numbers and j is the imaginary unit.
'''

# Strings

# Subsets of strings can be taken using the slice operator ([] and [:]) with indexes starting at 0 in the beginning of
# the string and working their way from -1 at the end.
# The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.

# SLICE OPERATOR
#   str[a:b] = AUSSCHLISSLICH b

str = 'Hello World!'

print(str)          # Prints complete string
print(str[:])       # Prints complete string
print(str[0])       # Prints first character of the string
print(str[0:1])     # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + " TEST")  # Prints concatenated string


# Python Lists
'''
The values stored in a list can be accessed using the slice operator ([] and [:]) with indexes starting at 0 in
the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator,
and the asterisk (*) is the repetition operator.
'''

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)             # Prints complete list
print(list[0])          # Prints first element of the list
print(list[1:3])        # Prints elements starting from 2nd till 3rd
print(list[2:])         # Prints elements starting from 3rd element
print(tinylist * 2)     # Prints list two times
print(list + tinylist)  # Prints concatenated lists


# Python Tuples
'''
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values
separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ([]) and their elements and
size can be changed, while tuples are enclosed in parentheses () and cannot be updated. Tuples can be thought
of as read-only lists.
'''

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)        # Prints the complete tuple
print(tuple[0])          # Prints first element of the tuple
print(tuple[1:3])     # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])       # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)     # Prints the contents of the tuple twice
print(tuple + tinytuple)  # Prints concatenated tuples

# tuple[2] = 1000    # Invalid syntax with tuple


# Dictionary

'''
Python Dictionary

Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found 
in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers 
or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).
'''

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(dict['one'])      # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)         # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values


# Data Type Conversion
'''
Sr.No. 	Function & Description
---------------------------------------------------------------------------------
1 	    int(x [,base])
        Converts x to an integer. base specifies the base if x is a string.
2 	    long(x [,base] )
        Converts x to a long integer. base specifies the base if x is a string.
3 	    float(x)
        Converts x to a floating-point number.
4 	    complex(real [,imag])
        Creates a complex number.
5 	    str(x)  
        Converts object x to a string representation.
6 	    repr(x)
        Converts object x to an expression string.
7 	    eval(str)
        Evaluates a string and returns an object.
8 	    tuple(s)
        Converts s to a tuple.
9 	    list(s)
        Converts s to a list.
10 	    set(s)
        Converts s to a set.
11 	    dict(d)
        Creates a dictionary. d must be a sequence of (key,value) tuples.
12 	    frozenset(s)
        Converts s to a frozen set.
13 	    chr(x)
        Converts an integer to a character.
14 	    unichr(x)
        Converts an integer to a Unicode character.
15 	    ord(x)
        Converts a single character to its integer value.
16 	    hex(x)
        Converts an integer to a hexadecimal string.
17 	    oct(x)
        Converts an integer to an octal string.
'''
