"""
Requirement: Last part of a string before a specified char
"""
# Using rsplit()
print("---------Using rsplit()----------")

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1))
print(str1.rsplit('/', 2))
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('/', 1)[1])
print(str1.rsplit('-', 1)[0])

x = 'http://test.com/lalala-134'
print(x.rsplit('-', 1)[0])
x = 'something-with-a-lot-of-dashes'
print(x.rsplit('-', 1)[0])

# Using rpartition()
print("---------Using rpartition()----------")
x = 'http://test.com/lalala-134'
print(x.rpartition('-'))
print(x.rpartition('-')[0])

x = 'something-with-a-lot-of-dashes'
print(x.rpartition('-')[0])

str1 = 'This is a sentence'
split_value = []
tmp = ''
for c in str1:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:                             # if tmp has a value it will add into split_value list in this case
    split_value.append(tmp)

print(split_value)
print(tmp)