
# EVerything is an object in python

def get_details(x,y):
    try:
        print("In try block")
        result = x/y  # Throwing exception ZeroDivisionError,  ZeroDivisionError("division by zero")
        print("Try block executed completely")
        print("Result is : ",result)
        # return result
    except ZeroDivisionError as zde:
        print("Please enter valid number for denominator :: ", zde)
        #2. print("Please enter valid number for denominator :: ")
        #3. print("Please enter valid number for denominator :: ")
        #3. print(zde)
    else:
        print("Else block executed")
    finally:
        print('Finally executed')  # closing operations

get_details(5, 0)

print("---Mulitiple excpiton hanlding-----------")

def get_data2(x,y):
    try:
        print("In try block")
        result = x/y  # Throwing exception ZeroDivisionError,  ZeroDivisionError("division by zero")
        print("Try block executed completely")
        print("Result is : ",result)
        # return result
    except ZeroDivisionError as zde:
        print("Please enter valid number for denominator :: ", zde)
    except TypeError as te:
        print("Please enter valid number for denominator :: ", te)
    except ValueError as ve:
        print("Please enter valid number for denominator :: ", ve)
    else:
        print("Else block executed")
    finally:
        print('Finally executed')  # closing operations

get_data2(5, 0)
# print(get_details(10, 5))

'''
In try except finally
- if exception didnt happen : try finally 
- if exception occurs       : try except finally

SC1 : Exception didn't occur
        1. try block will be executed completely.
        2. It will skip except block
        3. else block will be executed
        3. finally block will be executed
SC2 : Exception  occurs
        1. try block will be executed till exception line of code.
           It will stop executing lines of code after exception statement
        2. It will execute except block
        3. skips else block 
        3. finally block will be executed


Purpose of finally:
- If we opened in try block(db connections,files) we need to properly close them.
For that puprose we will use finally block

'''


'''
At line 7, python creates object for ZeroDivisionError class 
            ZeroDivisionError("division by zero")
            ZeroDivisionError as zde = ZeroDivisionError("division by zero")
Handling exception in except block     Throws exception in try block 
                
                
            ZeroDivisionError zde = ZeroDivisionError("division by zero")
            2L of CAN                2L  of Water
  
Animal 5L Can
Horse  2L Can  0.5L 1L 2L 3L 4L 5L 
Horse horse = new Horse();  # Above example
Animal anim = new Animal();
Animal anim1 = new Horse(); # Below example  // Upcasting
Animal anim1 = new Dog();     
Animal anim1 = new Lion();
Animal anim1 = new Cat();
Animal anim1 = new Rat();
Animal anim1 = new Bat();
'''
print("-------------------------------")
def get_data(x,y):
    try:
        print("In try block")
        result = x/y  # 2  ZDE TE
        list1 = [1,2,3,4]
        print(list1[5])  # 1 AIOR
        print("Try block executed completely")
        print("Result is : ",result)
    except Exception as exc:
        print("Please enter valid numbers :: ", exc)
    else:
        print("Else block executed")
    finally:
        print('Finally executed')  # closing operations
    print("End of method")
get_data(5,0)