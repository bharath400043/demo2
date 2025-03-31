"""
Step 1:  Input data   : given string
         Req(Question): String slicing
Step 2:  Retrieval    : get a piece of string b/w two index positions
Step 3:  Datatype     : String :
Step 4:  State :
         Behavior:
"""
str1 = "yogeswar reddy"
s = 0
msg = ''
for i in str1:
    if i == str1[s]:
        msg += str1[s]
        s += 1
print("accessing msg from index 0 to end: ", msg)

str1 = "python programming"
s = 3
msg = ''
for i in str1:
    if i == str1[s]:
        if s >= 3 and s <= 15:
            msg += str1[s]
            s += 1
print('slicing the message from 3 to 15 using algorithms: ', msg)


# slicing a string using function

def string_slicing():
    str1 = "python programming"
    s = 3
    msg = ''
    for i in str1:
        if i == str1[s]:
            if s >= 3 and s <= 15:
                msg += str1[s]
                s += 1
    return msg

print('slicing the message from 3 to 15 using algorithms: ', string_slicing())

# Wrong procedure
message = "python programming"
c = 3
d = 0
msg = ''
for i in message:
    if i == message[c]:
        if c >= 3 and d <= 15:
            msg += message[c]
            c += 1
            d += 1
print('slicing the message from 3 to 15 using algorithms: ', msg)