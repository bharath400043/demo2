

from _15_Decorators._5_Sum_with_Decorator import NumberException

def mulitply(num1, num2):
    res = num1 * num2
    return res


try:
    n1 = int(input("Enter number 1  :"))
    n2 = int(input("Enter number 2  :"))
    if n1 < 0 or n2 < 0:
        raise NumberException("Please enter positive number")
    result = mulitply(n1, n2)
    print("Sum of given numbers is :",result)
except NumberException as ne:
    print(ne)
