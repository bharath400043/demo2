# 2. NESTED FUNCTIONS :
print("---------------2. NESTED FUNCTIONS------------------")
def parent1():
    print("Before Nested Function")

    def first_child(): # nested function
        return "In nested func : first_child()"

    print("After Nested Function")

    print( first_child() )
    print( first_child )

    return first_child  # <function parent1.<locals>.first_child at 0x000001B0034A3BF8>
print(parent1)  # parent1 = <function parent1 at 0x000001BF373B1E18>   x = 10
# parent1.first_child()  This is not the way to call nested function

nest_func_addr = parent1()
print("Calling  nested function from outside function      : ",nest_func_addr())  # 12 line
print("Printing nested function name from outside function : ",nest_func_addr)    # 13 line

print("-----------------------------------------")

# print(parent1.first_child())
ch_addr = parent1()
print("Calling first child nested func ==> " ,ch_addr())
print("Printing first child nested func ==> " ,ch_addr)

# parent1.first_child() #We can't call nested function directly
print(ch_addr())


print("------Using EXCEPTION HANLDING ---------------- ")
try:
    parent1.first_child()
except AttributeError as err:
    print("Exception :: ",err)
    print("--You cannot call nested function directly------")

print("---------------------------------------------------")


