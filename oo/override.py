class Parent:
    def myMethod(self):
        print('Calling parent method')


class Child(Parent):
    def myMethod(self):
        print('Calling child method')


c = Child()          # instance of child
c.myMethod()         # child calls overridden method


# Base Overloading Methods
'''
Sr.No. 	Method, Description & Sample Call
--------------------------------------------
1 	__init__ ( self [,args...] )
    Constructor (with any optional arguments)
2 	__del__( self )
    Destructor, deletes an object
3 	__repr__( self )
    Evaluable string representation
4 	__str__( self )
    Printable string representation
5   __cmp__ ( self, x )
    Object comparison
'''
