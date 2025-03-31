'''
Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes
member methods : Methods (IM,CM,SM)


Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


madhu = Employee1(100,"MadhuN",15000)

Abstraction :
--------------
Hiding the implementation details in the methods of  a class

In a "Normal class" Abstraction is 0%
In "Abstract Class" Abstraction is 0-100 %
In an "Interface"   Abstraction is 100%

Inheritance :
---------------
super class, sub class mechanism

Polymorphism :
---------------
    - Static Polymorphism -- Method overloading
    - Dynamic Polymorphism -- Method overriding

'''


class Employee:
    # STATE --> data members
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # BEHAVIOR --> member methods
    def get_details(self):
        print("Employee details")


# Employee.get_details()
obj = Employee(1001, 'MadhuN', 10000)
obj.get_details()