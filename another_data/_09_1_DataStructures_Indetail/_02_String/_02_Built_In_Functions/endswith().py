"""
The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
Syntax: str.endswith(suffix[, start[, end]])
* suffix - String or tuple of suffixes to be checked
* start (optional) - Beginning position where suffix is to be checked within the string.
* end (optional) - Ending position where suffix is to be checked within the string.
* It returns True if strings ends with the specified suffix.
* It returns False if string doesn't end with the specified suffix.
"""

# endswith() Without start and end Parameters
text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)

# endswith() With start and end Parameters
text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)