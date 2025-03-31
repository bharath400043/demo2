"""
Function Definition:
def : Keyword
sum : Function name
()  : Paranthesis
num1,num2 : parameters
lines under function : business logic
"""

"""
def sum():
    pass
"""

# Function definition
def sum():
    print("Inside function")

# Function call / Invocation
sum()
print("After function")

x = 10   # variable = value

list1 = [1,2,3,4]

# def append(object)  # Function definition : object --> parameter

list1.append(10)      # Function calling    : 10     --> argument

# variable = value
# parameter = argument

def sum(num1, num2):
    res = num1 + num2
    print("sum of two numbers: ", res)

"""
Function calling:
sum --> Function name
10,20 --> Arguments"""

# Approach 1
sum(10, 20)   # 10, 20 arguments
# Approach 2
n1 = 10    # n1 -> variable  10-> value
n2 = 20
sum(n1, n2)   # n1, n2 are arguments

# Approach 3
n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
sum(n1, n2)

print("---------------------")
# Basic call of functions
def sub(num1, num2):
    res = num1 - num2
    print("Substraction of two numbers: ", res)
sub(50,25)
print(sub(40, 25))
