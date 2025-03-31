# Simple inheritance
class Employee:
    def __init__(self):
        print("Emp constructor")
    def get_hike(self, exp): # behavior
        print("Employee hike applied")   # implementation

class PvtEmployee(Employee):
    def __init__(self):
        print("PVt Constructor")

class GovtEmployee(Employee):
    def __init__(self):
        pass
print("-----Employee-------")
emp = Employee()
emp.get_hike(10)
print("-----Pvt Employee-------")
pemp = PvtEmployee()
pemp.get_hike(12)



class Student(object):
    def __init__(self):
        print("In Student constructor")

    def get_data(self):
        print("In Student method")

stu = Student()
stu.get_data()