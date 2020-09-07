# Assertions
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
# print(KelvinToFahrenheit(-5))


# Exceptions
# After the except clause(s), you can include an else-clause. The code in the else-block executes
# if the code in the try: block does not raise an exception.
'''
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# You can also use the except statement with no exceptions defined as follows.
'''
try:
   You do your operations here;
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''

# The except Clause with Multiple Exceptions
'''
try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''

# The try-finally Clause
# You can use a finally: block along with a try: block. The finally block is a place to put any code
# that must execute, whether the try-block raised an exception or not. You cannot use else
# clause as well along with a finally clause.
'''
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
'''

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print("Error: can't find file or read data")


try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can't find file or read data")


# Argument of an Exception
'''
try:
   You do your operations here;
   ......................
except ExceptionType as Argument:
   You can print value of Argument here...
'''

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.args)
