# Passing Arguments
'''
1. Positional argument (Required argument).
2. Default argument.
3. Keyword argument (Named argument)
'''
# 1. Positional argument (Required argument)
print("--------1. Positional argument--------------")
def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum is : ",res)

sum(10, 20, 30)


# 2. Default arguments
print("--------2. Default arguments-------------")
def sum(n1, n2, n3 = 1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)

sum(10,20)
sum(10,20,30)

'''
n3 = 1000
n3 = 30
'''


def sum(n1, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)

sum(10)
sum(10,20)
sum(10,20,30)
# sum(10,20,30,40)

'''
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)

* we can get error with this function because we can't pass non-default parameters after default parameter
'''
# 3. Keyword argument (Named argument)
print("--------3. Keyword argument-------------")
def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum is : ",res)

#sum(10,20,30)
sum(n2 = 10, n3 = 20, n1 = 30)


def sum(n1, n2, n3=45):
    res = n1 + n2 + n3
    print("Sum is : ",res)

#sum(10,20,30)
sum(n2 = 10, n3 = 20, n1 = 30)
sum(n2 = 10, n1 = 30)
sum(n1 = 30, n2 = 10) # sum(30,10)