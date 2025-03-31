"""
The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.
Syntax: str.startswith(prefix[, start[, end]])
* prefix - String or tuple of strings to be checked
start (optional) - Beginning position where prefix is to be checked within the string.
end (optional) - Ending position where prefix is to be checked within the string.
* startswith() method returns a boolean.
It returns True if the string starts with the specified prefix.
It returns False if the string doesn't start with the specified prefix.
"""

# startswith() Without start and end Parameters

text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)

#  startswith() With start and end Parameters
text = "Python programming is easy."

# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)

# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('program', 7, 18)
print(result)

# startswith() With Tuple Prefix
text = "programming is easy"
result = text.startswith(('python', 'programming'))
# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))
# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)
# prints False
print(result)
result = text.startswith(('programming', 'easy'), 15, 19)
print(result)
