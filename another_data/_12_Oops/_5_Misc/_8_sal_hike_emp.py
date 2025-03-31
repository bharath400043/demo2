
# Employee salary hike
# CRUD        STATE            BEHAVIOR
# UPDATE      eid ,name ,sal   update_hike

# Using Functions Approach:3

empid = 1000     # int(input("Enter empid"))
ename = 'MadhuN' # input("Enter name ")
salary = 20000   # float(input("Enter salary "))

def update_hike(eid, name, sal):
    sal = sal + sal * 15 / 100
    print("Emp details after hike : ",eid,name,sal)

update_hike(empid ,ename ,salary)

# Using OOPS     Approach:4
class Employee:

    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def update_hike(self,rating):
        print("Emp details Before : ", self.eid, self.name, self.sal)
        self.sal = self.sal + self.sal * 15 / 100
        print("Emp details After  : ", self.eid, self.name, self.sal)

'''
empid = int(input("Enter empid"))
ename = input("Enter name ")
salary = float(input("Enter salary "))
madhu = Employee(empid,ename,salary)
'''

madhu = Employee(100,'Madhu Nettem',20000)   # OBJECT/INSTANCE CREATION  , madhu is an object/instance/reference variable
print(madhu)
madhu.update_hike()

x = 10
x = x + 10   # 100    ATM Card 100 rs
print(type(10),type(10.5),type(True),type("Madhu"),type([1,2,3]),type((1,2,3)),type({1:1}),type({1,2,3}))
print(x)
'''
class int:
    def __init__(self, x, base=10):
'''

age = 10
print("age ",age)


name = 'Madhu'

'''
class : : Logical => STATE    
          Phyical => BEHAVIOR

object :: Physial => STATE
          Logical => BEHAVIOR
'''

li1 = list([1,2,3])  # [1,2,3]
print(li1)
