import os

print("Python is really a great language,", "isn't it?")

# str = input("Enter your input: ")
# print("Received input is : ", str)


# str = input("Enter your input: ")
# print("Received input is : ", eval(str))


# file object = open(file_name [, access_mode][, buffering])

'''
    file_name − The file_name argument is a string value that contains the name of the file that you want to access.

    access_mode − The access_mode determines the mode in which the file has to be opened, i.e., read, write, 
    append, etc. A complete list of possible values is given below in the table. This is optional parameter and the 
    default file access mode is read (r).

    buffering − If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line 
    buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 
    1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system
     default(default behavior).
'''


file = open("test.txt", "r+")

print(file.closed)
print(file.mode)
print(file.name)

# file.write("Python is a great language.\nYeah its great.\n")

str = file.read(10)
print("Read String is: ", str)

file.close()

# File Positions
fo = open("test.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)

fo.close()

# os.rename("test2.txt", "test3.txt")
# os.remove("test3.txt")


# Directories in Python
# os.mkdir("newDir")

# os.chdir("newDir")
os.getcwd()

# deletes the directory, which is passed as an argument in the method.
# Before removing a directory, all the contents in it should be removed.

# os.rmdir('dirname')


# close
fo = open("test.txt", "r")
print("Name of the file: ", fo.name)
fo.close()

fo = open("test.txt", "r")
print("Name of the file: ", fo.name)
fo.flush()
fo.close()

fo = open("test.txt", "r")
print("Name of the file: ", fo.name)
print("File Descriptor: ", fo.fileno())
fo.close()

#  isatty() returns True if the file is connected (is associated with a terminal device)
#  to a tty(-like) device, else False.
fo = open("test.txt", "r")
print("Name of the file: ", fo.name)
print(fo.isatty())
fo.close()


fo = open("test.txt", "r")
line = fo.readline()
print("Read Line: %s" % (line))
line = fo.readline(5)
print("Read Line: %s" % (line))
fo.close()


fo = open("test.txt", "r")
line = fo.read(10)
print("Read Line: %s" % (line))
fo.close()


fo = open("test.txt", "r")
line = fo.readlines()
print("Read Line: %s" % (line))
line = fo.readlines(2)
print("Read Line: %s" % (line))
fo.close()


fo = open("test.txt", "a")
seq = ["This is 6th line\n", "This is 7th line\n"]
fo.writelines(seq)
fo.close()

fo = open("test.txt", "r")
line = fo.readlines()
print("Read Line: %s" % (line))
fo.close()

