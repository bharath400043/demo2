# Simple Inheritence
print("-----------Simple Inheritence-------------")

class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name =name
        self.sal = sal

    def get_emp_details(self):
        print("employee details")

class SoftwareEmployee(Employee):
    def __init__(self):
        pass
    def emp_hike(self):
        print("software employee hike")
yogi = SoftwareEmployee()
yogi.emp_hike()
yogi.get_emp_details()
print(yogi)    # def __str__():

# Multilevel inheritence
print("-----------Multilevel inheritence-------------")

class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name =name
        self.sal = sal

    def get_emp_details(self):
        print("employee details")

class SoftwareEmployee(Employee):
    def __init__(self):
        pass
    def emp_hike(self):
        print("software employee hike")

class BackendDeveloper(SoftwareEmployee):
    def __init__(self):
        pass
    def emp_skills(self):
        print("Backend developer skills")
    def __str__(self):                           # Method Overriding
        return "Get backend developer details instead of address"

yash = BackendDeveloper()
yash.get_emp_details()
yash.emp_hike()
yash.emp_skills()
print(yash)

# Hierarchial Inhiertance
print("-----------Hierarchial Inhiertance-------------")
class Animal:
    def __init__(self):
        pass
    def eating(self):
        print("Have eating behaviour")

class Cat(Animal):
    def __init__(self):
        pass
    def running(self):
        print("Cat has running behaviour")

class Dog(Animal):
    def __init__(self):
        pass
    def barking(self):
        print("Dog has barking behaviour")

snoopy = Dog()
snoopy.barking()
snoopy.eating()

# Multiple Inheritence
print("-----------Multiple Inheritence-------------")
class A:
    def m1(self):
        print("A m1()")

class B:
    def m1(self):
        print("B m1()")

class C(A, B):
    def m2(self):
        print("C m2()")

sub = C()
sub.m1()     # object will check m1() method first in A class
sub.m2()