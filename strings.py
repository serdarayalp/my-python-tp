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

txt = "My name is Ståle"

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))

encoded = txt.encode(encoding="ascii", errors="replace")
print(encoded)

print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))


# str.decode(encoding='UTF-8',errors='strict')
print(encoded.decode(encoding="ascii", errors="xmlcharrefreplace"))