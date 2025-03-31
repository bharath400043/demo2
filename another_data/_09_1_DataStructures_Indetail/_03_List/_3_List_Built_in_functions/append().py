"""
append(): The append() method adds an item to the end of the list
syntax: list.append(item)
* The method takes a single argument
item - an item to be added at the end of the list
The item can be numbers, strings, dictionaries, another list, and so on.
"""
fruits = ["apple", "banana", "mango"]
print("fruits: ", fruits)
fruits.append("grapes")   # adding an element into a list
print("fruits after append an elem: ", fruits)

dry_fruits = ["dates", "walnuts"]
fruits.append(dry_fruits)      # adding a list of elements into a list and it will add as a list in list
print("fruits after append a list of fruits: ", fruits)
""" if we want to add list of elements into a list as elements for old list we can use extend() instead of append()"""
