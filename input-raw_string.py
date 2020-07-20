'''
Developers often have a need to interact with users, either to get data or to provide some sort of result. 
Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python 
provides us with two inbuilt functions to read the input from the keyboard.

* input (prompt)
* raw_input (prompt) 

input() function
-------------------
Python input() function is used to take the values from the user. This function is called to tell the program to 
stop and wait for the user to input the values. It is a built-in function. The input() function is used in both 
the version of Python 2.x and Python 3.x. In Python 3.x, the input function explicitly converts the input you 
give to type string. But Python 2.x input function takes the value and type of the input you enter as it is 
without modifying the type.#
'''

import sys

name = input("Enter the name: ")

# print the type of input value
print(type(name))
print(name)

number = input("Enter the number: ")

print('Type Vorher: ', type(number))

number = int(number)
print('Type Nachher: ', type(number))

print(number)


'''
raw_input() function
--------------------------
Python raw_input function is used to get the values from the user. We call this function to tell the program 
to stop and wait for the user to input the values. It is a built-in function. 

This function is used only in Python 2.x version. 
'''


'''
Python 2:
    * raw_input() übernimmt genau das, was der Benutzer eingegeben hat und gibt es als Zeichenfolge zurück. 
    * input() nimmt zuerst den Wert aus der raw_input() Funktion und führt dann auch eine eval() aus. 

Python 3:
    * raw_input() wurde in input() umbenannt, daher gibt input() die genaue Zeichenfolge zurück.
    * Alte input() wurde entfernt. Wenn Sie die alte input() verwenden möchten, müssen Sie sie manuell mit 
        eval(input()) ausführen.
'''


# Multiple Statements on a Single Line
# x = 'foo'; sys.stdout.write(x + '\n');

'''
Multiple Statement Groups as Suites

A group of individual statements, which make a single code block are called suites in Python. 
Compound or complex statements, such as if, while, def, and class require a header line and a suite.

Header lines begin the statement (with the keyword) and terminate with a colon (:) and are followed by one or 
more lines which make up the suite.

if expression: 
   suite
elif expression: 
   suite 
else: 
   suite
'''

