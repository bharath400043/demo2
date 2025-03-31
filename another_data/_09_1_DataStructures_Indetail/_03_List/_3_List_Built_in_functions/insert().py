"""
The list insert() method inserts an element to the list at the specified index.
Syntax:list.insert(i, elem)
The insert() method takes two parameters:
*index - the index where the element needs to be inserted
*element - this is the element to be inserted in the list
*The insert() method doesn't return anything; returns None. It only updates the current list.
*If anything other then a list is used with insert(), then it returns an AttributeError.
"""
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "orange")
print("updated list: ", fruits)

vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')
print('Updated List:', vowel)

#  Inserting a Tuple (as an Element) to the List
mixed_list = [{1, 2}, [5, 6, 7]]
# number tuple
number_tuple = (3, 4)
# inserting a tuple to the list
mixed_list.insert(1, number_tuple)
print('Updated List:', mixed_list)

# attribute error
string = "1234567"
string.insert(10, 1)
# print(string)   AttributeError: 'str' object has no attribute 'insert'