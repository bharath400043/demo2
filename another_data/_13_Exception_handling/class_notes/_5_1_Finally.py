'''
Created on Dec 9, 2019

@author: madhu
'''
id = 10

print(id) 

try:
    raise KeyboardInterrupt("KEY")

except KeyboardInterrupt as err:
    print("Good Bye !!!",err)

finally:
    print("Finally executed")



class Employee(object):
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

madhu = Employee(100,"MadhuSudhaN",10000)
print(madhu) # __str_l