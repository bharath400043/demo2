'''
@author: madhu
'''
'''
Created on 20-Jun-2017

@author: yugan
'''
from test.test_typing import Employee


class Employee:
    pass


err = ZeroDivisionError("Zero error")

# Exception  err = ZeroDivisionError("Zero error")

print(err)
'''
ZeroDivisionError err = ZeroDivisionError("division by zero")
'''

def get_number(x, y):
    
    try:
        print("-----IN TRY BLOCK--------")
        result = x / y
        print("The result for division is : ",result)
        float_res = round(24.601 / 0.01234, 4.6)
    except Exception as err:
        print("---Error is bening handled by super class Exception-----")
        """  
        except ZeroDivisionError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except TypeError as err:
            print("Plese check the calculation :::  ",err)
        except OverflowError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except Exception as err:
            print("---------------")
             
        """
    else:
        print("--------In ELSE block---------")

    finally:
        print("------Executing finally block--------------")
    
get_number(20,0)

