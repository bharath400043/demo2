
class NumberException(Exception):
    def __init__(self,message):
        self.messsage = message


def sum(num1, num2):
    res = num1 + num2
    return res

'''
@ Here this logic is aceepting negative numbers also
n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))
print(sum(n1,n2))
'''

# To avoid that one till now we have used exception hanlding
try:
    n1 = int(input("Enter number 1  :"))
    n2 = int(input("Enter number 2  :"))
    # Validation logic
    if n1 < 0 or n2 < 0:
        raise NumberException("Please enter positive number")
    result = sum(n1, n2)
    print("Sum of given numbers is :",result)
except NumberException as ne:
    print(ne)

try:
    if n1 < 0 or n2 < 0:
        raise NumberException("Please enter positive number1")
except NumberException as ne:
    print(ne)
# Now onwards use Decorator
