

class Employee(object):
    def __init__(self):  # eid,name,sal
        pass

    def get_hike(self):
        print("Getting Employee data")

class GovtEmployee(Employee):   # GovtEmployee is-a Employee
    def __init__(self):   # pf, gratuity
        pass

class PvtEmployee(Employee):    # PvtEmployee is-a Employee
    def __init__(self):  # pf
        pass

    def get_hike(self):  # method overriding
        print("Getting Pvt Employee data")  # our own implementation

gemp = GovtEmployee()
gemp.get_hike()

pvemp = PvtEmployee()
pvemp.get_hike()

# is - a relationship


class Animal:
    pass

class Employee(Animal):
    pass

# Employee is a Animal  is-a --> fails

