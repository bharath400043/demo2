# 3. RETURNING FUNCTIONS
print("---------------3. RETURNING NESTED FUNCTION NAME------------------")

def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    if num == 10:
        return first_child
    else:
        return second_child
'''
    try:
        assert num == 10
        print("Assertion is True.Continue to execute the remaining code")
        return first_child  # returning function name
    except AssertionError:
        return second_child # returning function name
    finally:
        print("Finally executed")
'''

xyz = parent(10)

print("*************")
print("Returning function name FC : " ,xyz)
print("Executing function FC      : " ,xyz())
print("*************")

abc = parent(11)
print("Returning function name SC : " ,abc)
print("Executing function SC      : " ,abc())

print("-------------------------------------")
def parent1():
    def first_child():
        return "In First Child"
    return first_child

print("Calling parent1 function : ",parent1() )
x = parent1()
print("Calling parent1 function : ",x() )
print("Calling parent1 function : ",parent1()())