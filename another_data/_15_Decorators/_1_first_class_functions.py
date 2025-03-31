
def sum1(num1, num2):
    res = num1 + num2
    #print("result is ", res)
    return res

#1
print("Type 1 :",sum1(10,20)) # print(10)
#2
output = sum1(10, 20)
print(output)   # x = 10 print(x)

#3
sum1(10,20)  # print stmt YES return stmt NO

x = 10
print(x, type(x))
print("Function details  ",sum1, type(sum1))
x = 10
y = 20
print("Sum call ", sum1(x, y))

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1. First Class functions
2. Nested Functions
3. Returning Functions
'''

def foo(bar):
    #print("Output is :",bar + 1)
    return bar + 1
# 1
foo(10) # if print statement is there inside function
# 2
print(foo(10)) # if return stmt exists
# 3
x = foo(10)   # if return stmnt exits and output is being used in 2 or more places
print(x)

print("Comparision :", foo(2) == 3+10)  # functions return a value based on the given arguments.
'''
                Steps execution:
                1. foo(2) - function call   will get response         ==> 3   
                2. 3+10   - perform arithmetic ops. and give result   ==> 13
                3. compare function response with arithm ops result   ==> 3 == 13  => False
                4. Give result to print function
                
                
                print("Comparision ", 10)      # 0
                print("Comparision ", 10+20)   # 1
                print("Comparision ", 10+20 == 30)   # 2
                print("Comparision ", 10+20 == 10+30)   # 3
                print("Comparision ", foo(10+20) == 10+30)   # 4
'''


def foo2(bar):
    return bar + 1


foo2(2)
print(foo2(3))
print(type(foo2))
print(foo2)


# 1. FIRST CLASS FUNCTIONS:
print("============1. FIRST CLASS FUNCTIONS=============")

'''
Here foo_func requires function name why because we have used 
the same parameter during function call

X            Y            Z        =>   X Y  True 
Amar        Balaji      Chanakya       Y Z  True    
foo(bar)    media()    get_data()

functionname
arguments 
'''


print("----With out first class function  Z->X -----------")
def foo(bar):       # Function X
    return bar + 1

def get_data():        # Function Z
    res = foo(100)  # We are calling other function from our function
    print("Val from foo is : ",res)

get_data()

print("----With First Class function  Z->Y->X -----------")
def foo(bar):    # X
    return bar + 1

def mediator(foo_func, val):  # Y
    output = foo_func(val) # foo(100)
    return output

def get_daata():  # Z
    res = mediator(foo, 100)
    print("Val from foo is : ",res)

get_daata()
print("------------------------------------")

