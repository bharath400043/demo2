'''def __new__(cls,*args,**kwargs):
        print(cls)
        print("*args =",*args)
        print("**kwargs =",**kwargs)
  '''
 # http://agiliq.com/blog/2012/06/__new__-python/
# http://spyhce.com/blog/understanding-new-and-init


class Employee:
    x = 10
    '''
    def __new__(cls,*args = None,**kwargs = None):
        new_instance = object.__new__(cls,*args,**kwargs)
        setattr(new_instance, 'created_at', datetime.datetime.now())
        return new_instance
    '''
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        print("INIT gets called")
        print("self IS : ",self)

    def get_grade(self):
        print("-----------inside get method----------")

madhu = Employee(100,'Madhu Nettem',90000)
print("Madhu object details ",madhu.id," ",madhu.name)
madhu.get_grade()

'''
0. Python while loading the class, initializes the class variables
During object creation
1. Instantiation : Python Interpreter will check the class address, __new__ method will get called and 
                   passes 1.classname(Employee), 2.arguments(100,'Madhu Nettem',90000)
                   Here empty object will be created(wrapper chocolate) and 
                   it will pass wrapper address to self parameter and other args to __init__ parameters
2. Initialization: Inside init method state will be initialized in wrapper

'''

list1 = [1,2,3]  # CREATE
print(list1)     # RETRIEVAL
list1.append(10) # UPDATE
del list1        # DELETE

list1 = list([])
#madhu = Employee()
print(list1)

num = int()
print(num)
bo = bool()
f_val = float()
str_val = str()
t_val = tuple()
dict1 = dict()
set1 = set()
print(num,f_val,bo, str_val,t_val,dict1,set1)