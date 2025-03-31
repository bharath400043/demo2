# https://www.programiz.com/python-programming/operator-overloading
# https://www.geeksforgeeks.org/operator-overloading-in-python/

# Python program to show use of  + operator for different purposes.

print(1 + 2)   # 1.__add__(2)
print("Geeks" + "For")
print(3 * 4)
print("Geeks" * 4)

x = 10
# x.__add__()
y = 20
print(x+y)  # x.__add__(y)
print(10 == 20) # 10.__eq__(20)

'''
class Employee:
    def __init__(self,sal):
        self.sal = sal

madhu = Employee(1000)
kiran = Employee(2000)
print(madhu+kiran)
'''

# With Operator overloading with +
class Employee:
    def __init__(self,sal):
        self.sal = sal

    # adding two objects
    def __add__(self, obj):
        return self.sal + obj.sal

madhu = Employee(1000)
kiran = Employee(2000)
print("Adding 2 emp objects ",madhu+kiran)   # madhu.__add__(kiran)

# With Operator overloading with gt >=

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, obj):
        if(self.marks > obj.marks):
            return True
        else:
            return False
    def __eq__(self, obj):
        if(self.marks == obj.marks):
            return True
        else:
            return False
madhu = Student(25)
prakash = Student(32)
if(madhu < prakash):
    print("Madhu got marks greater than Prakash")
else:
    print("Prakash got marks greater than Madhu")