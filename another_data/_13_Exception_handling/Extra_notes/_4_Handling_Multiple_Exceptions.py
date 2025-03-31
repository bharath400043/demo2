'''
@author: madhu
https://docs.python.org/2.7/tutorial/appetite.html
https://docs.python.org/2.7/tutorial/errors.html
'''
# S O L I D principles
'''
ATMCard:
    10 methods 5 - debitcard
               5 - creditcard
DebitCard:   CreditCard:
    5           5
High Level Class <---Abstraction--->  Low Level class
Class                 I/AC                  Class

   Employee           Vehicle          Car   Bike   Cycle 
     m1():                fuel()        x()
                          mileage()  
                        
 
            Vehicle v = Car()  
            v.fuel()
            v.mileage()
            v.x()
'''
class MyClass(object):

    def getDetails(self):
        count = 0
        while True:
            try:
                count += 1
                print(count)
                if count > 3:
                    return 'Account Blocked'
                x = int(input("Please enter number"))
                res = x + 10
                print("Entered value is :",x)
                # .....
                #break
            except (ValueError,TypeError,NameError,OSError):
            # except Exception as e:
                print("Please enter valid input :: ")
            else:
                print("ELSE block executed")
            finally:
                print("Finally executed")

my=MyClass()
print(my.getDetails())


print("------------------------------")


from pip._vendor.distlib.compat import raw_input


try:  
    num1 =int(raw_input("Enter num1"))
    num2 =int(raw_input("Enter num2"))
    result = num1/num2
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except (ZeroDivisionError,IOError) as err:
    print("Exception occured :",err)
else:
    print("Successfully Executed")
finally:
    print("Finally executed")


'''
SC1 : Exception didn't occur
        1. try block will be executed completely.
        2. It will skip except block
        3. else block will be executed
        3. finally block will be executed
SC2 : Exception  occurs
        1. try block will be executed till exception line of code.It will stop executing lines of code after exception statement
        2. It will execute except block
        3. skips else block 
        3. finally block will be executed

'''
'''
Exception
    ZeroDivisionError

Animal
  Dog
  Cat 
  
my_list = [1,2,3,4]
1. Animal a = new Animal()       a = Animal()
2. Dog    d = new Dog()          d = Dog()
3. Animal d = new Dog()  -- Upcasting  2L MH into 5L can
4. Dog    d = new Animal() X -- Downcasting
'''