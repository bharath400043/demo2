"""
class Employee:
    comp_name = "TCS"
    comp_loc = "Banglore"
    def __init__(self, eid, name, sal):      # parameterized constructor
        self.eid = eid
        self.name = name
        self.sal = sal
    @classmethod
    def comp_details(cls):
        print("company details: ", cls.comp_name, cls.comp_loc)

    def get_emp_details(self):       # Instance method
        print("emp details: ", self.eid, self.name, self.sal, Employee.comp_name, Employee.comp_loc)

    def get_hike(self, rating, sal):
        if rating > 2.5:
            sal = sal + sal * 20 / 100
        print("salary after hike: ", sal)

    @staticmethod
    def emp_rules(list1):
        print("Rules for employees: ")
        for i in list1:
            print(i)

list1 = ["Time management", "Entry card", "proper dress"]
yogi = Employee(101, "Yogesh", 20000)
yogi.get_emp_details()
yogi.get_hike(3, 20000)
yogi.comp_details()
yogi.emp_rules(list1)

"""
"""
class Employee:
    def __init__(self):      # default constructor
        pass
    def get_emp_details(self, rating = None, sal = 15000):  # method overloading
        print("emp details: ", sal,",", rating)

yogi = Employee()
yogi.get_emp_details()
yogi.get_emp_details(5)
yogi.get_emp_details(2, 10000)

"""

class Employee:
    def __init__(self, eid, name, sal = 25000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_emp_details(self):  # Instance method
        print("emp details: ", self.eid, self.name, self.sal)

    def get_hike(self, rating = 1, sal = 25000):       # method overloading
        if rating > 2.5:
            sal = sal + sal * 20 / 100
        print("salary after hike: ", sal)

yogi = Employee(101, "Yogesh")
yogi.get_emp_details()
yogi.get_hike()
yogi.get_hike(4, 20000)
