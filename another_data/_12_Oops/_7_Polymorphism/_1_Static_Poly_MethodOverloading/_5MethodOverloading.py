'''
Created on 29-Jul-2017

@author: madhu
'''

# http://thepythonguru.com/python-args-and-kwargs/
'''
Function Definition: 
    parameters - Yes           No
      -normal args   
          - limited  
              - declared params
                  - type of param
                      .......
              
              - default params
          - Unlimited *args
          
      - keywros args (**kwargs)
'''          
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
'''
print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )
print_values("Alex","Gray","Harper","Phoenix","Remy","Val")
'''             
class Addition:
    
    def __init__(self,id=10):
        pass
    
    def add(self,num1 = [],*args):
        # print(type(num1))
        # num1.append()
        if num1 is int:
            print(num1," INT")
        else:
            print(num1)
        for i in args:
            print(i)
    
    def addit(self,**kwargs):
        for key,value in kwargs.items():
            print(key," ",value)
                         
obj=Addition()
obj.add(10)     
print("-----------------------")  
obj.add("MAD",1,2,3,4,5,6,78)
print("-----------------------")  
obj.addit(x="1",y="2")
print("-----------------------")  

my_data={'1':'10','2':'20','3':'30'}
obj.addit(**my_data)
print("-----------------------")  



