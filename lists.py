list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# slicing
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# update
list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001
print("New value available at index 2 : ")
print(list[2])

# del oder remove
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del(list1[2])
print("After deleting value at index 2 : ")
print(list1)

# Basic List Operations
print(len([1, 2, 3])) 	# 3, Length
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6], Concatenation
print(['Hi'] * 4)  # ['Hi', 'Hi', 'Hi', 'Hi'], Repetition
print(3 in [1, 2, 3])  # True, Membership

for x in [1, 2, 3]:
    print(x)  # 1 2 3, Iteration

L = ['spam', 'Spam', 'SPAM!']
print(L[2])
print(L[-2])
print(L[1:])

# Built-in List Functions & Methods

list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print("First list length : ", len(list1))
print("Second list length : ", len(list2))


list1, list2 = ['xyz', 'zara', 'abc'], [456, 700, 200]
print("Max value element : ", max(list1))
print("Max value element : ", max(list2))
print("Min value element : ", min(list1))
print("Min value element : ", min(list2))


'''
Sr.No. 	Methods with Description
---------------------------------
1 	    list.append(obj)
        Appends object obj to list
2 	    list.count(obj)
        Returns count of how many times obj occurs in list
3 	    list.extend(seq)
        Appends the contents of seq to list
4 	    list.index(obj)
        Returns the lowest index in list that obj appears
5 	    list.insert(index, obj)
        Inserts object obj into list at offset index
6 	    list.pop(obj=list[-1])
        Removes and returns last object or obj from list
7 	    list.remove(obj)
        Removes object obj from list
8 	    list.reverse()
        Reverses objects of list in place
9 	    list.sort([func])
        Sorts objects of list, use compare func if given
'''