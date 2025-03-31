"""
The rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).
Syntax: string.rstrip([chars])
* The rstrip() removes characters from the right based on the argument (a string specifying the set of characters to be removed).
* chars (optional) - a string specifying the set of characters to be removed.
If chars argument is not provided, all whitespaces on the right are removed from the string.
* The rstrip() returns a copy of the string with trailing characters stripped.
* All combinations of characters in chars argument are removed from the right of the string until first mismatch
"""

random_string = ' this is good'
# Leading whitepsace are removed
print(random_string.rstrip())
# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))

print(random_string.rstrip('sid oo'))

website = 'www.programiz.com/'
print(website.rstrip('m/.'))

str = "     this is string example....wow!!!     "
print(str.rstrip())
str = "88888888this is string example....wow!!!8888888"
print(str.rstrip('8'))

string = "geekssss"
# Removes given set of characters from
# right.
print(string.rstrip('s'))

string = "   for    "
# Leading whitespaces are removed
print("Geeks" + string.rstrip() + " Geeks ")

string = "geeks for geeks"
# Argument doesn't contain trailing 's'
# So, no characters are removed
print(string.rstrip('ek'))

string = "geeks for geeks"
# Removes given set of characters from
# right.
print(string.rstrip('ske'))