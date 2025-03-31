"""The remove() method removes the first matching element (which is passed as an argument) from the list.
Syntax: list.remove(element)
*The remove() method takes a single element as an argument and removes it from the list.
*If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
*The remove() doesn't return any value (returns None).
"""
# Remove element from the list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# 'rabbit' is removed
animals.remove('rabbit')
# Updated animals List
print('Updated animals list: ', animals)

# remove() method on a list having duplicate elements
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
# 'dog' is removed
animals.remove('dog')
# Updated animals list
print('Updated animals list: ', animals)

# Deleting element that doesn't exist
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
# Deleting 'fish' element
# animals.remove('fish')
# Updated animals List
print('Updated animals list: ', animals)

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# looping till all 1's are removed
while (list1.count(1)):
    list1.remove(1)

print(list1)
