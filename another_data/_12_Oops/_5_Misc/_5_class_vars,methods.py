# Class with instance variables,instance methods


# BEFORE

class Employee:   # This apporach is wrong

    #1.STATE
    def __init__(self, eid, name, sal, office):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.office = office  # Declare this as class variable

    #2.BEHAVIOR
    def get_emp_details(self):
        print("Emp details are :",self.eid,self.name,self.sal,self.office)

madhu = Employee(101,'Madhu Nettem',15000,'ORACLE')
madhu.get_emp_details() # ==> Employee.get_emp_details(madhu)
prakash = Employee(102,'PrakashS',20000,'ORACLE')
kiran = Employee(103,'Kiran Kumar',25000,'ORACLE')


'''
 Disadvantage with above code :
 We are using common/sharable (office) data in __init__ method
which causes memory waste.Make it as class variable as below
'''
print("---------------With class variables,class Methods---------------")
class Employee:
    # class variable
    office = 'ORACLE' # Initialized while class loading
    caddress = "Whitefield,Bangalore"

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    @classmethod
    def get_comp_name(cls):  # class method
        print("Get company name : ", cls.office, cls.caddress)

    def get_emp_details(self):
        name = self.name
        names = name.split(" ")
        print(name.count('N'))
        print(names)
        #print("Emp details are :",self.eid, self.name, self.sal, Employee.office, Employee.caddress)  # self.office

name = "Madhu Nettem"
names = name.split(" ")
print("outside class ",name.count('N'))

Employee.get_comp_name()
# Employee.get_emp_details()

madhu = Employee(101,'Madhu Nettem',15000)
madhu.get_emp_details()

'''
Class variable     : Will be initialized when class is loaded by interpreter 
                        and memory allocation will be done at the loading itself
Instance variable : When we create an object for class,these will get initialized
'''


# Different ways of creating class

# 1. only class vars,  class methods

class Employee:
    office = 'ORACLE'
    '''
    def __init__(self):
        pass
    '''
    @classmethod
    def get_info(cls):
        print("Class EMP DATA :", cls.office)

Employee.get_info()
emp = Employee()
emp.get_info()   # This is not proper way of calling


# 2. only instance vars, instance methods            # Refer _4_instance_vars_methods.py

# 3. Combination of instance,class vars, methods      # Refer 28th line

'''
Class vars     Class methods      YES
Instance vars  Instance Methods   YES
Class vars     Instance Methods   YES
Instance vars  Class methods       NO
'''

# Static methods

class Employee:

    @staticmethod
    def sum(a,b):
        res = a+b
        print("I am in static method",res)

Employee.sum(20,30)

'''
Class structure:
-----------------

class Employee:
    
    #1. Class variables
    #2. Instance variables
    
    #3  Class Methods      
    #4  Instance Methods
    #5  Static Methods

eid name salary mobileno emalid office o_adress e_address attendance empcount (sharable+Modifiable)
I   I      I     I          I     C       C       I          C          C

9AM - 10
10AM - 30
12PM - 70

4PM - 90
5PM - 50
7PM - 50
0

100 -> 101 -> 90
'''

