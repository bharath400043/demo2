"""Requirement : Find length of a given string"""
name = input(str("enter a string: "))

# Built in functions
print("length of string: ", len(name))

# Without built in function

length = 0
for each in name:
    length += 1
print("Length of given string: ", length)

print("----Using Functions-------")
def findlen(str):
    length = 0
    for each in str:
        length += 1
    return length
str = findlen("python")
print("Length of string: ", str)

def findlen(str):
    length = 0
    while str[length:]:
        length += 1
    return length
str = findlen("program")
print("Length of string: ", str)


def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1      # "ypyopygpyepyspyh"
str = "yogesh"
print("Length of string: ", findLen(str))
