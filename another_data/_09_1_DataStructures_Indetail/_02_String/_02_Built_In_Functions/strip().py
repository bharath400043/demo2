"""
The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
* The strip() method removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).
Syntax: string.strip([chars])
* chars (optional) - a string specifying the set of characters to be removed from the left and right part of the string.
* If the chars argument is not provided, all leading and trailing whitespaces are removed from the string.
* strip() returns a copy of the string with both leading and trailing characters stripped.
* When the character of the string in the left mismatches with all the characters in the chars argument, it stops removing the leading characters.
* Similarly, when the character of the string in the right mismatches with all the characters in the chars argument, it stops removing the trailing characters.
"""

string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))

string = """    geeks for geeks    """

# prints the string without stripping
print(string)

# prints the string by removing leading and trailing whitespaces
print(string.strip())

# prints the string by removing geeks
print(string.strip(' geeks'))

str1 = 'geeks for geeks'
# Print the string without striping.
print(str1)

# String whose set of characters are to be
# remove from original string at both its ends.
str2 = 'ekgs'

# Print string after striping str2 from str1 at both its end.
print(str1.strip(str2))