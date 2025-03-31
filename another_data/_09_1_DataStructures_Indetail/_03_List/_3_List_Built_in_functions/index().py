"""
The index() method returns the index of the specified element in the list.
Syntax:list.index(element, start, end)
Parameters:
element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index
* The index() method returns the index of the given element in the list.
* If the element is not found, a ValueError exception is raised.
* The index() method only returns the first occurrence of the matching element.
"""
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)
# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')
print('The index of i:', index)

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# Will print the index of '4' in list1
print(list1.index(4))
list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
# Will print the index of 'cat' in list2
print(list2.index('cat'))

# Working of index() With Start and End Parameters
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)
# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)
# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!   ValueError: 'i' is not in list
print('The index of i:', index)

# Random list having sublist and tuple also
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]
# Will print the index of sublist [9, 8, 7]
print(list1.index([9, 8, 7]))
# Will print the index of tuple
# ('cat', 'bat') inside list
print(list1.index(('cat', 'bat')))