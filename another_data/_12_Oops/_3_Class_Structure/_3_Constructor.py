'''
STATE --> BEHAVIOR

0. Python while loading the class, initializes the class variables
During object creation
1. Instantiation : Python Interpreter will check the class address, __new__ method will get called and
                   passes 1.classname(Employee), 2.arguments(100,'Madhu Nettem',90000)
                   Here empty object will be created(wrapper chocolate) and
                   it will pass wrapper address to self parameter and other args to __init__ parameters
2. Initialization: Inside init method state will be initialized in wrapper

Default constructor
Parameterized constructor

Constructor calling:
---------------------
Positional args
Default args
keywords args

'''
# Default constructor
class Employee:
    def get_data(self,edata):
        print("Emp Id : ",edata['eid'])

emp = Employee()
emp.get_data({'eid':100})

# Single responsibility principle

# Default constructor
class Employee:
    def __init__(self):   # Default constructor
        pass

    def get_data(self,edata):
        print("Emp Id : ",edata['eid'])

emp = Employee()
emp.get_data({'eid':100})

# Parameterized constructor

# Positional arguments
class Employee:
    # constructor
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal


madhu = Employee(101,'Madhu N',10000)


# Default arguments
class Employee:
    # constructor
    def __init__(self, eid, name, sal=10000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal


madhu = Employee(101, 'Madhu N')
madhu = Employee(101, 'Madhu N',25000)

# Keyword arguments
class Employee:
    # constructor
    def __init__(self, eid, name, sal=10000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal


madhu = Employee(101, 'Madhu N')
madhu = Employee(name = 'Madhu N',sal = 25000, eid = 2001)