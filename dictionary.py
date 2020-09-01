dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])


dict = {'Name': 'Zara', 'Age': 7}
print("Start Len : %d" % len(dict))
dict.clear()
print("End Len : %d" % len(dict))

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = dict1.copy()
print("New Dictionary : %s" % str(dict2))


seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("New Dictionary : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("New Dictionary : %s" % str(dict))


dict = {'Name': 'Zabra', 'Age': 7}
print("Value : %s" % dict.get('Age'))
print("Value : %s" % dict.get('Education'))
print("Value : %s" % dict.get('Education', "Never"))

dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" % dict.setdefault('Age', None))
print("Value : %s" % dict.setdefault('Sex', None))

dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" % dict.items())

dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" % dict.keys())


dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}
dict.update(dict2)
print("Value : %s" % dict)

dict = {'Name': 'Zara', 'Age': 7}
print("Value : %s" %  dict.values())
