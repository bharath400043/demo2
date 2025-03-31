# Return Statement
list1 = [1, 2, 3, 4]
print(list1)
print(list1.append(5))
print(list1)
print(list1.extend([10, 20, 30]))
print(list1)
print(list1.remove(3))
print(list1)
print(list1.pop())
print(list1)

"""
remove : remove will remove the given value from list and return None
pop   : pop will remove the value from list and return the same value
"""
print("------------------")
# Approach 1
def sum(num1, num2):
    res = num1 + num2
    print("Sum of two numbers: ", res)
sum(20, 30)

# Approach 2.1
def sum(num1, num2):
    res = num1 + num2
    return res
sum(10, 20)  # No use when return statement given in function
print("Sum of two numbers : ", sum(10, 20))

# Approach 2.2
def sum(num1, num2):
    res = num1 + num2
    return res
output = sum(10, 20)
print("Sum of two numbers: ", output)

# Approach 3
def sum(num1, num2):
    res = num1 + num2
    return res
n1 = 10
n2 = 30
output = sum(n1, n2)
print("Sum is: ", output)

print("---------------------")
print(10)  # 2.1   When the particular value is used only once in entire program

x = 10
print(x)   # 2.2   When the particular value is used in mulitple places

print("---------------------")
# Find wheather given number is even or odd
# STATE
n = 25
# Behavior
if n % 2 == 0:
    print("even number")
else:
    print("odd number")

print("----- Using Functions------")
n = 23   # variable, value
def is_even_odd(num):  # parameter
    if num % 2 == 0:     # variable
        print("even number")
    else:
        print("odd number")

is_even_odd(n)   # argument
print(is_even_odd(n))     # no use to print


n1 = 20
def is_even_odd(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

# no use
is_even_odd(n1)
# 1st Action
print("number is: ", is_even_odd(n1))

# 2nd action
res = is_even_odd(n1)
print("Number is: ",res)

list1 = [1,2,3,4]
print("list before :  ",list1)
list1.append(5) # CORRECT
'''
print(list1.append(5))
res = list1.append(5)
'''
print("list append :  ",list1)

list1.pop()  # WRONG
print("Element popped : ",list1.pop())

val = list1.pop()
print("Element popped : ",val)

s1 = {1,2,3,4,5}
print("Before discard : ",s1)
s1.discard(3)
print("After discard : ",s1)


print(10)
x = 10
print(x)
print(10+20)

emp_id = 195
def emp_data(id):
    emp_id = 25    # Variable , value
    print("Hello world", emp_id)    # the emp_id will take in side value of variable
    return emp_id * emp_id
    # print("End of program")  # No use of write because it won't execute after return statement
print("Outside function: ", emp_id)
print(emp_data(emp_id))
print("Outside function: ", emp_id)

def get_details():
    print("Hello world")
    return # number, string,bool,list,tuple,dict,set
           # operations arith logical .....
    # return 10+20+30

def hello(num):
    return
print(hello(10))

def fun():
    str = "geeksforgeeks"
    x = 20
    return [str, x]
list = fun()
print(list)


def fun():
    d = dict()
    d['str'] = "GeeksforGeeks"
    d['x'] = 20
    return d
d = fun()
print(d)

print("----------------")
def create_adder(x):
    def adder(y):
        return x + y

    return adder
add_15 = create_adder(15)

print("The result is", add_15(20))

