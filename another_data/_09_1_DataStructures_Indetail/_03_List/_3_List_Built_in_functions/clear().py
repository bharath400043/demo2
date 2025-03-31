"""
The clear() method removes all items from the list.
Syntax: list.clear()
* The clear() method doesn't take any parameters.
* The clear() method only empties the given list. It doesn't return any value.
"""

list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()
print('List:', list)

# Emptying the List Using del
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]
print('List:', list)