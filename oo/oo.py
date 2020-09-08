class Employee:

    # The class has a documentation string, which can be accessed via ClassName.__doc__.
    'Common base class for all employees'

    # Class variable:
    #   A variable that is shared by all instances of a class. Class variables are
    #   defined within a class but outside any of the class's methods.
    # This can be accessed as Employee.empCount from inside the class or outside the class.
    empCount = 0

    # Instance variable:
    #   A variable that is defined inside a method and belongs only to the current instance of a class.

    # __init__() is a special method, which is called class constructor or initialization method that Python
    # calls when you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # You declare other class methods like normal functions with the exception that the first argument
    # to each method is self. Python adds the self argument to the list for you; you do not need to include
    # it when you call the methods.
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)


emp1.age = 7  # Add an 'age' attribute.
print(emp1.age)
# emp1.age = 8  # Modify 'age' attribute.
# print(emp1.age)
# del(emp1.age)  # Delete 'age' attribute.
# print(emp1.age)

print(hasattr(emp1, 'age'))   # Returns true if 'age' attribute exists
print(getattr(emp1, 'age'))    # Returns value of 'age' attribute
setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
print(getattr(emp1, 'age'))
# delattr(emp1, 'age')    # Delete attribute 'age'


# Built-In Class Attributes
print(emp1.__dict__)
print(emp1.__doc__)
# Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print(emp1.__module__)

# --------------------------------------------------------------------

from point import Point

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
del(pt1)
del(pt2)
del(pt3)


class Parent:

    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):

    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the 
# superclass sup.

# The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of 
# a subclass of Class

