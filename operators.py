'''
Python language supports the following types of operators.
    * Arithmetic Operators
    * Comparison Operators
    * Assignment Operators
    * Logical Operators
    * Bitwise Operators
    * Membership Operators
    * Identity Operators
'''

a = 2
b = 4

# Arithmetic Operators
# ----------------------------------
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)  # Exponent (a hoch b)

c = 9
d = 2
print(c / d)
# Floor Division: The division of operands where the result is the quotient in which the
print(c // d)
# digits after the decimal point are removed.


# Comparison Operators

if a == b:
    print('beide sind gleich')
if a != b:
    print('beide sind nicht gleich')
if a > b:
    print('a ist größer als b')
if a < b:
    print('a ist kleiner als b')
if a >= b:
    print('a ist größer oder gleich als b')
if a <= b:
    print('a ist kleiner oder gleich als b')
