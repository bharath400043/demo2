"""
Requirement : Convert given strig into all uppercase
"""

# Using upper() built-in-function

str1 = "Yogeswar reddy"
print(str1.upper())

# Using function
def uppercase(str_data):
    result = ''
    for char in str_data:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
print(uppercase('acdé--#λ'))


def toUppercase(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in s:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i>= 26:
            result += x
        else:
            result += alphabet[i+26]
    return result

print(toUppercase("YogeswaR"))


def toUppercase(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in s:
        if x not in alphabet or alphabet.index(x)>=26:
            result += x
        else:
            result += alphabet[alphabet.index(x)+26]
    return result
print(toUppercase("yogeswar@Reddy"))