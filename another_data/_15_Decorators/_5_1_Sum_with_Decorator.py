
class NumberException(Exception):
    def __init__(self,message):
        self.messsage = message

'''
  1 first class funciton
  2 nested function
  3 returning nested function
  4 *args **kwargs
'''
'''
try:
    if n1 < 0 or n2 < 0:
        raise NumberException("Please enter positive number")
except NumberException as ne:
    print(ne)
'''
'''
def validate_numbers(func): # func = sum
    def wrapper(*args,**kwargs):  # *args = n1 n2
        if args[0] >= 0 or args[1] >= 0:
            res = func(*args)  # sum(n1, n2)
            return res
        else:
        raise NumberException("Please enter positive number")
    return wrapper
'''
'''
def validate_numbers(func): # func = sum
    print("----Inside validate_numbers decorator-----")
    def wrapper(*args,**kwargs):  # *args = n1 n2
        print("----Inside wrapper-----")
        if args[0] >= 0 or args[1] >= 0:
            res = func(*args)  # sum(n1, n2)
            return res
        else:
            print("Please enter Positive numbers only")
    return wrapper
'''


def validate_numbers(func): # func = sum
    def wrapper(*args,**kwargs):  # *args = n1 n2
        if args[0] >= 0 and args[1] >= 0:
            res = func(*args)  # sum(n1, n2)
            return res
        else:
            print("Please enter Positive numbers only")
    return wrapper

@validate_numbers
def sum(num1, num2):
    print("----Inside sum function-----")
    res = num1 + num2
    return res


n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))
result = sum(n1, n2)
print("Sum of given numbers is :",result)

#    X     Y      Z

@validate_numbers
def sub(n1,n2):
    pass
@validate_numbers
def mul(n1,n2):
    pass

@validate_numbers
def div(n1,n2):
    pass
