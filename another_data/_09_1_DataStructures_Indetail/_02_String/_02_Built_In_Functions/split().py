"""
The split() method breaks up a string at the specified separator and returns a list of strings.
Syntax: str.split([separator [, maxsplit]])
* separator (optional)- It is a delimiter. The string splits at the specified separator.
If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
* maxsplit (optional) - The maxsplit defines the maximum number of splits.
The default value of maxsplit is -1, meaning, no limit on the number of splits.
* split() breaks the string at the separator and returns a list of strings.
"""

text= 'Love thy neighbor'
# splits at space
print(text.split())
grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.split(', '))
# Splitting at ':'
print(grocery.split(':'))

# How split() works when maxsplit is specified?
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.split(', ', 2))
# maxsplit: 1
print(grocery.split(', ', 1))
# maxsplit: 5
print(grocery.split(', ', 5))
# maxsplit: 0
print(grocery.split(', ', 0))

text = 'geeks for geeks'
# Splits at space
print(text.split())
word = 'geeks, for, geeks'

# Splits at ','
print(word.split(','))
word = 'geeks:for:geeks'
# Splitting at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'
# Splitting at 3
print([word[i:i + 3] for i in range(0, len(word), 3)])
