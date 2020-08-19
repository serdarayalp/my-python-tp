import math
import random

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
print(math.exp(math.pi))  # 23.1406926328

# This method returns largest integer not greater than x.
print("math.floor(-45.17): ", math.floor(-45.17))
print("math.floor(100.12): ", math.floor(100.12))
print("math.floor(100.72): ", math.floor(100.72))
print("math.floor(119L): ", math.floor(119))
print("math.floor(math.pi): ", math.floor(math.pi))


# The natural logarithm of a number is its logarithm to the base of the mathematical constant e
print("math.log(100.12): ", math.log(100.12))
# log10() returns base-10 logarithm
print("math.log(100): ", math.log10(100))

print("max(80, 100, 1000): ", max(80, 100, 1000))
print("min(80, 100, 1000): ", min(80, 100, 1000))

# modf() returns the fractional and integer parts of x in a two-item tuple.
# Both parts have the same sign as x. The integer part is returned as a float.
print("math.modf(100.12): ", math.modf(100.12))

# pow() returns x to the power of y. If the third argument (z) is given, it returns x to the power of y
# modulus z, i.e. pow(x, y) % z.
print("math.pow(100, 2) : ", math.pow(100, 2))

# round() returns x rounded to n digits from the decimal point.
print("round(80.23456, 2) : ", round(80.23456, 2))
print("round(80.23456, 3) : ", round(80.23456, 3))
print("round(80.23456, 4) : ", round(80.23456, 4))
print("round(80.23456, 5) : ", round(80.23456, 5))

print("math.sqrt(100) : ", math.sqrt(100))


# Random Number Functions

# choice() returns a random item from a list, tuple, or string.
print("choice([10, 20, 30, 40, 50]) : ", random.choice([10, 20, 30, 40, 50]))
print("choice('Das ist ein Test') : ", random.choice('Das ist ein Test'))

# randrange() returns a randomly selected element from
#     randrange ([start,] stop [,step])
''' 
    start − Start point of the range. This would be included in the range.
    stop − Stop point of the range. This would be excluded from the range.
    step − Steps to be added in a number to decide a random number.
'''
# Select an even number in 100 <= number < 1000
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
# Select another number in 100 <= number < 1000
print("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))

# random() returns a random float r, such that 0 is less than or equal to r and r is less than 1.
# 0 <= r < 1
print("random() : ", random.random())


# seed() sets the integer starting value used in generating random numbers.
# Call this function before calling any other random module function.

# seed(x): x is the seed for the next random number. If omitted, then it takes system time to generate next random number.
random.seed(10)
print("Random number with seed 10 : ", random.random())

# shuffle() randomizes the items of a list in place.
list = [20, 16, 10, 5]
random.shuffle(list)
print("Reshuffled list : ",  list)

# uniform() returns a random float r, such that x is less than or equal to r and r is less than y. 
#   x <= r < y
print("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
