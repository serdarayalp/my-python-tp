import base64

str = "Hello World"

# Slicing
print("str[0]: ", str[0])
print("str[1:5]: ", str[1:5])

# Update Strings
print(str[:6] + 'Python')

a = "Hello"
b = "Python"
print(a + b)
print(a * 2)
print(a[1])
print(a[1:4])  # ell
print("H" in a)
print("S" not in a)


# String Formatting Operator
print("My name is %s and weight is %d kg." % ('Max', 65))

'''
Format Symbol 	Conversion
-------------------------------
%c 	            character
%s 	            String-Konvertierung mittels str() vor der Formatierung
%i 	            signed decimal integer
%d 	            signed decimal integer
%u 	            unsigned decimal integer
%o 	            octal integer
%x 	            hexadecimal integer (lowercase letters)
%X 	            hexadecimal integer (UPPERcase letters)
%e 	            exponential notation (with lowercase 'e')
%E 	            exponential notation (with UPPERcase 'E')
%f 	            floating point real number
%g 	            the shorter of %f and %e
%G 	            the shorter of %f and %E
'''

# Triple Quotes

triple = """Das ist 
ein \n Test"""
print(triple)

s = 'Hi\nHello'
print(s)

# raw string
s = r'Hi\nHello'
print(s)

s = u'Hi\nHello'
print(s)


# Built-in String Methods

str = "das ist ein Test..."
print(str.capitalize())

str = "Das ist ein Test"
print(str.center(100, '*'))

# str.count(substring, start= 0, end=len(string))
str = "Das ist ein Test"
print(str.count("i"))

# str.encode(encoding='UTF-8',errors='strict')
'''
    encoding − This is the encodings to be used. For a list of all encoding schemes please visit.
                A String specifying the encoding to use. Default is UTF-8
        https://docs.python.org/3/library/codecs.html#standard-encodings

    errors − This may be given to set a different error handling scheme. The default for errors is 'strict', 
    meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 
    'backslashreplace' and any other name registered via codecs.register_error().

    A String specifying the error method. Legal values are:
    -----------------------------------------------------------------------------------------------
    'backslashreplace'	- uses a backslash instead of the character that could not be encoded
    'ignore'	- ignores the characters that cannot be encoded
    'namereplace'	- replaces the character with a text explaining the character
    'strict'	- Default, raises an error on failure
    'replace'	- replaces the character with a questionmark
    'xmlcharrefreplace'	- replaces the character with an xml character    
'''

str = "My name is Ståle"

print(str.encode(encoding="ascii", errors="backslashreplace"))
print(str.encode(encoding="ascii", errors="ignore"))
print(str.encode(encoding="ascii", errors="namereplace"))

encoded = str.encode(encoding="ascii", errors="replace")
print(encoded)

print(str.encode(encoding="ascii", errors="xmlcharrefreplace"))


# str.decode(encoding='UTF-8',errors='strict')
print(encoded.decode(encoding="ascii", errors="xmlcharrefreplace"))

str = "Das ist ein Test"
suffix = "Test"
print(str.endswith(suffix))


str = "Das\tist ein Test"
print(str)
print(str.expandtabs())
print(str.expandtabs(16))


# str.find(str, beg=0, end=len(string))
# return: index if found and -1 otherwise.
str1 = "Das ist ein Test"
str2 = "ist"
print(str1.find(str2))

# rfind(str, beg=0,end=len(string))
# Same as find(), but search backwards in string.

# index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.

# rindex( str, beg=0, end=len(string))
# Same as index(), but search backwards in string.

str = "dasisteinTest123456"  # No space in this string
print(str.isalnum())

str = "Das ist ein Test"
print(str.isalnum())

# isalpha(): Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
# isdigit(): Returns true if string contains only digits and false otherwise.
# islower(): Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
# isnumeric(): Returns true if a unicode string contains only numeric characters and false otherwise.

str = "Das Ist Ein Test"
print(str.istitle())
str = "Das ist ein Test"
print(str.istitle())


# isupper(): Python string method isupper() checks whether all the case-based characters (letters) of the string are uppercase.

'''
Python string method join() returns a string in which the string elements of sequence have been joined by str separator.
Syntax: str.join(sequence)
'''
trenner = ","
seq = ("a", "b", "c")
print(trenner.join(seq))

# len(string) : Länge des Texts

# str.ljust(width[, fillchar])
# rjust(width,[, fillchar])
# Python string method ljust() returns the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space).
# The original string is returned if width is less than len(s).
str = "Das ist ein Test"
print(str.ljust(50, '0'))
print(str.rjust(50, '0'))

# lower(): Converts all uppercase letters in string to lowercase.
# upper(): Converts lowercase letters in string to uppercase.

# isdecimal(): Returns true if a unicode string contains only decimal characters and false otherwise.

'''
Python string method strip() returns a copy of the string in which all chars have been stripped from the 
beginning and the end of the string (default whitespace characters).

Syntax: str.strip([chars])
'''
str = "0000000Das ist ein Test0000000";
print(str.strip('0'))

# str.lstrip([chars])
# rstrip(): Removes all trailing whitespace of string.
# Python string method lstrip() returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters).
str = "     Das ist ein Test.     "
print(str.lstrip())
str = "88888888Das ist ein Test.8888888"
print(str.lstrip('8'))


str = "this is a sample example"
print(str.replace("is", "was"))
print(str.replace("is", "was", 1))


# str.split(str="", num=string.count(str)).
# Python string method split() returns a list of all the words in the string, using str as the separator 
# (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.

# split(): This method returns a list of lines.
str = "Das ist ein Test";
print(str.split())
print(str.split(' ', 1 ))


str = "Das ist ein Test";
print(str.startswith('Das'))

# str.zfill(width): Python string method zfill() pads string on the left with zeros to fill width.
str = "Das ist ein Test";
print(str.zfill(50))