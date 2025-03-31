"""
The pop() method removes the item at the given index from the list and returns the removed item.
syntax: list.pop(index)
*The pop() method takes a single argument (index).
*The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
*If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
* The pop() method returns the item present at the given index. This item is also removed from the list.

"""
languages = ['Python', 'Java', 'C++', 'French', 'C']
# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)


"""Requirement: A list fruit contains fruit_name and property saying its fruit.
Another list consume has two items juice and eat. With the help of pop() and append() we can do something interesting.
"""
fruit = [['Orange', 'Fruit'], ['Banana', 'Fruit'], ['Mango', 'Fruit']]
consume = ['Juice', 'Eat']
possible = []

# Iterating item in list fruit
for item in fruit:

    # Inerating use in list consume
    for use in consume:
        item.append(use)
        possible.append(item[:])
        item.pop(-1)
print(possible)