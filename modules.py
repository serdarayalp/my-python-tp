# import ModuleName
# import module1[, module2[,... moduleN]

# import specific attributes from a module
# from ModuleName import name1[, name2[, ... nameN]]

# to import the function fibonacci from the module fib
# from fib import fibonacci

# to import all names from a module
# from ModuleName import *

'''
Locating Modules
--------------------------------
When you import a module, the Python interpreter searches for the module in the following sequences −
    * The current directory.
    * If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
    * If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
'''


# Namespaces and Scoping
'''
A Python statement can access variables in a local namespace and in the global namespace. 
If a local and a global variable have the same name, the local variable shadows the global variable.

Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned a 
value in a function is local.
'''


import math
Money = 2000


def AddMoney():
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)

# dir() built-in function returns a sorted list of strings containing the names defined by a module.
content = dir(math)
print(content)

# ----------------------------------------------

# The globals() and locals() Functions

'''
The globals() and locals() functions can be used to return the names in the global and local 
namespaces depending on the location from where they are called.

If locals() is called from within a function, it will return all the names that can be accessed locally 
from that function.

If globals() is called from within a function, it will return all the names that can be accessed globally 
from that function.

The return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function.
'''

total = 0  # This is global variable.


def sum(arg1, arg2):
    total = arg1 + arg2  # Here total is local variable.
    # so kann man eine globale Variable ändern, die den selben Namen mit einer lokalen Variable hat
    # globals()['total'] = arg1 + arg2
    print("Inside the function local total : ", total)
    return total


sum(10, 20)
print("Outside the function global total : ", total)
