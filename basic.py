# Python Identifiers
'''
A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts 
with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive 
programming language. Thus, Manpower and manpower are two different identifiers in Python.

Here are naming conventions for Python identifiers −

    * Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
    * Starting an identifier with a single leading underscore indicates that the identifier is private.
    * Starting an identifier with two leading underscores indicates a strongly private identifier.
    * If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
'''

# Lines and Indentation
if True:
    print('True')
else:
    print('False')


# Multi-Line Statements
'''
Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation 
character (\) to denote that the line should continue.

total = item_one + \
        item_two + \
        item_three

Statements contained within the [], {}, or () brackets do not need to use the line continuation character.

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
'''


# Quotation in Python
# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same
# type of quote starts and ends the string.
# The triple quotes are used to span the string across multiple lines.

word = 'word'
sentence = "This is a sentence."

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

paragraph = '''This is a paragraph. It is
made up of multiple lines and sentences.'''

# Comments in Python

# First comment
print('Hello, Python!')  # second comment

'''
This is a multiline
comment.
'''
