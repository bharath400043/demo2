"""
count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.
Syntax: list_name.count(object)
* Object is the things whose count is to be returned.
* count() method returns count of how many times obj occurs in list.
* If more then 1 parameter is passed in count() method, it returns a TypeError.
"""
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)

# Count Tuple and List Elements Inside List
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
# count element ('a', 'b')
count = random.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count)
# count element [3, 4]
count = random.count([3, 4])
# print count
print("The count of [3, 4] is:", count)

list1 = [('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'),
         ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2]]
# Counts the number of times 'Cat' appears in list1
print(list1.count(('Cat', 'Bat')))
# Count the number of times sublist
# '[1, 2]' appears in list1
print(list1.count([1, 2]))

list1 = [1, 1, 1, 2, 3, 2, 1]
# Error when two parameters is passed.
# print(list1.count(1, 2))   TypeError: count() takes exactly one argument (2 given)