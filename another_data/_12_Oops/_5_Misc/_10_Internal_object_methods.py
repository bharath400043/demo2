class Employee(object):
    """This is employee class"""
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # Employee class has 3 behaviors
    def get_emp_hike(self,sal = 1000):
        pass

    def get_emp_desn(self,hike):
        pass

    def xyz(self):
        pass


madhu = Employee(100,"MadhuNettem",10000)  #CREATE


# Built in class attributes '''
print("---------------Built in class attributes-----------------")
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

print("---------------Built in object methods-----------------")
# Object Functions   C R U D
print("Has salary : ", hasattr(madhu, "sal"))          # RETRIEVE : Check whether object has speicific attribute exists or not
print("Set name   : ", setattr(madhu, "name", "MAD"))   # UPDATE   : To update field' value in existing object
print("Get name   : ", getattr(madhu, "name"))          # RETRIEVE
print("Del salary : ", delattr(madhu, "sal"))           # DELETE
#print("Get salary : ",getattr(madhu, "sal"))

'''
Employee.__dict__: {'__module__': '__main__', 
                    '__doc__'        : This is employee class,
                    '__init__'       :  <function Employee.__init__ at 0x000002AE97942BF8>, 
					'get_emp_hike'   : <function Employee.get_emp_hike at 0x000002AE97942C80>, 
					'get_emp_desn'   : <function Employee.get_emp_desn at 0x000002AE97942D08>,
					'xyz'            : <function Employee.xyz at 0x000002AE97942D90>, 
					'__dict__'       : <attribute '__dict__' of 'Employee' objects>, 
					'__weakref__'    : <attribute '__weakref__' of 'Employee' objects>, 
					}
Employee.__doc__: This is employee class
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
'''