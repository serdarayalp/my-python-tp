
# While
count = 0
while count < 10:
    print("The count is:", count)
    count = count + 1

# While mit ELSE:
#   If the else statement is used with a while loop, the else statement is executed when the condition becomes false.
count = 0
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")


# For-Schleife

# Syntax:
# for iterating_var in sequence:
#   statements(s)

for letter in 'Python':
    print("Current Letter :", letter)


fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print("Current fruit :", fruit)


for i in range(10, 20):
    print(i)


# Loop Control Statements

# break:
#   Terminates the loop statement and transfers execution to the statement immediately following the loop.

#   If you are using nested loops, the break statement stops the execution of the innermost loop and start
#   executing the next line of code after the block.

for letter in 'Python':
    if letter == 'h':
        break
    print("Current Letter :", letter)

var = 10
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break


# continue:
#   Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.

for letter in 'Python':
    if letter == 'h':
        continue
    print("Current Letter :", letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)

# pass: pass is a null operation. when it is executed, nothing happens. It is useful as a placeholder
# when a statement is required syntactically, but no code needs to be executed

def myPassFunction(param): pass    # a function that does nothing (yet)
# class C: pass    # a class with no methods (yet)