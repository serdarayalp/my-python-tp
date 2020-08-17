import math
'''
Python supports four different numerical types:
    * int (signed integers): 
        They are often called just integers or ints, are positive or negative whole numbers with no decimal point.
    * long (long integers ): 
        Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or 
        lowercase L.
    * float (floating point real values): 
        Also called floats, they represent real numbers and are written with a decimal point dividing the integer 
        and fractional parts. Floats may also be in scientific notation, with E or e indicating the power 
        of 10 (2.5e2 = 2.5 x 102 = 250).
    * complex (complex numbers) − are of the form a + bJ, where a and b are floats and J (or j) represents the square 
        root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. 
        Complex numbers are not used much in Python programming.
'''

'''
Number Type Conversion:

Python converts numbers internally in an expression containing mixed types to a common type for evaluation. 
But sometimes, you need to coerce a number explicitly from one type to another to satisfy the requirements of an 
operator or function parameter.

    * Type int(x) to convert x to a plain integer.
    * Type long(x) to convert x to a long integer.
    * Type float(x) to convert x to a floating-point number.
    * Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
    * Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. 
        x and y are numeric expressions
'''


# Mathematical Functions

# abs(x): The absolute value of x, the  positive distance between x and zero.

print(abs(10))
print(abs(10.0))
print(abs(-10))
print(abs(-10.0))

# fabs(x): The absolute value of x, the  positive distance between x and zero.
#   Der Unterschied zwischen abs() und fabs() besteht darin, dass math.fabs(number) immer eine Fließkommazahl zurückgibt, 
#   auch wenn das Argument ganzzahlig ist, während abs() je nach Argument ein Fließkomma oder eine Ganzzahl zurückgibt.
print(math.fabs(10))
print(math.fabs(10.0))
print(math.fabs(-10))
print(math.fabs(-10.0))

# ceil(x): The ceiling of x: the smallest integer not less than x
print(math.ceil(99))  # 99
print(math.ceil(99.1))  # 100
print(math.ceil(-45.1))  # -45
print(math.ceil(math.pi))  # 4


# Python number method exp() returns returns exponential of x: e hoch x
print(math.exp(math.pi)) # 23.1406926328
