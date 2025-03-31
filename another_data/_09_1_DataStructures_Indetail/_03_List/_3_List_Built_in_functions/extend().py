"""
The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
Syntax:list1.extend(iterable)
* Here, all the elements of iterable are added to the end of list1.
* The extend() method takes an iterable such as list, tuple, string etc.
* The extend() method modifies the original list. It doesn't return any value.

"""

language = ['French', 'English']
# another list of language
language1 = ['Spanish', 'Portuguese']
# appending language1 elements to language
language.extend(language1)
print('Language List:', language)


# Add Elements of Tuple and Set to List
language = ['French']
# language tuple
language_tuple = ('Spanish', 'Portuguese')
# language set
language_set = {'Chinese', 'Japanese'}
# appending language_tuple elements to language
language.extend(language_tuple)
print('New Language List:', language)
# appending language_set elements to language
language.extend(language_set)
print('Newer Language List:', language)

# extend() Vs append()
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)
# a1 = [1, 2, 3, 4]
a1.extend(b)
print(a1)
# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)