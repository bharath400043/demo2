"""
The reverse() method reverses the elements of the list
Syntax: list.reverse()
* The reverse() method doesn't take any arguments.
* The reverse() method doesn't return any value. It updates the existing list.
"""

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]
# updated list
print('Updated List:', reversed_list)

# Accessing Elements in Reversed Order
systems = ['Windows', 'macOS', 'Linux']
# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

"""
# error when string is used in place of list 
string = "abgedge" 
string.reverse()  
print(string)
"""

# practical application of reverse()
list1 = [1, 2, 3, 2, 1]
# store a copy of list
list2 = list1.copy()
# reverse the list
list2.reverse()
# compare reversed and original list
if list1 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")
