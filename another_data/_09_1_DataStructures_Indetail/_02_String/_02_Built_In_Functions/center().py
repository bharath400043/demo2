"""
The center() method returns a string which is padded with the specified character.
Syntax: string.center(width[, fillchar])
* width - length of the string with padded characters
* fillchar (optional) - padding character
* The fillchar argument is optional. If it's not provided, space is taken as default argument.
* The center() method returns a string padded with specified fillchar. It doesn't modify the original string.
"""

# center() Method With Default fillchar
string = "Python is awesome"
new_string = string.center(24)
print("Centered String: ", new_string)

# center() Method With * fillchar
string = "Python is awesome"
new_string = string.center(24, '*')
print("Centered String: ", new_string)