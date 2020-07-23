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


# Bitwise Operators

a = 60  # 0011 1100
b = 13  # 0000 1101

print(a & b)  # 12 = 0000 1100
print(a | b)  # 61 = 0011 1101
print(a ^ b)  # 49 = 0011 0001, XOR
print(~a)  # -61 = 1100 0011
print(a << 2)  # 240 = 1111 0000, bedeutet Wert*2 für jede Schiebeoperation
print(a >> 2)  # 15 = 0000 1111, bedeutet Wert/2 für jede Schiebeoperation

# Logical Operators
print(True and False)
print(True or False)
print(not(True))

# Membership Operators
l = [1, 2, 3, 4, 5]
print(2 in l)
print(20 not in l)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is  present in given list")


# Identity operators

# The == operator compares the value or equality of two objects, whereas the Python is operator 
# checks whether two variables point to the same object in memory.

x = 5
if (type(x) is int):
    print("true")
else:
    print("false")


# You can use id() to check the identity of an object:
# This line shows the memory address where the built-in function id itself is stored.
print(id(id))


