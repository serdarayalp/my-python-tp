def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


printme('Das ist ein Test...')

# ------------------------ Pass by reference vs value
# All parameters (arguments) in the Python language are passed by reference.

# Required arguments


def changeme(mylist):
    "This changes a passed list into this function"
    # mylist.append([1, 2, 3, 4])
    mylist = [1, 2, 3, 4]
    print("Values inside the function: ", mylist)


mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

# -----------------------------------------------

# Keyword arguments


def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)


printinfo(age=50, name="miki")


# Default arguments
def printinfo2(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)


# Now you can call printinfo function
printinfo2(age=50, name="miki")
printinfo2(name="miki")


# Variable-length arguments
def printinfo3(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# Now you can call printinfo function
printinfo3(10)
printinfo3(70, 60, 50)


# The Anonymous Functions
# sum = lambda arg1, arg2: arg1 + arg2
def sum(arg1, arg2): return arg1 + arg2


print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))


# return
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


total = sum(10, 20)
print("Outside the function : ", total)


# ----------------- globale und lokale Variablen

total = 0  # This is global variable.


def sum(arg1, arg2):
    total = arg1 + arg2  # Here total is local variable.
    # so kann man eine globale Variable ändern, die den selben Namen mit einer lokalen Variable hat
    # globals()['total'] = arg1 + arg2 
    print("Inside the function local total : ", total)
    return total


sum(10, 20)
print("Outside the function global total : ", total)
