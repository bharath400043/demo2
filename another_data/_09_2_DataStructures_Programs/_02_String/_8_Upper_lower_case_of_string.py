# using swapcase()
msg1 = "it will come uppercase"
msg2 = "IT WILL COME LOWERCASE"
msg3 = "iT Will cOMe MIxeDCaSe"
# using built in function

print(msg1.swapcase())
print(msg2.swapcase())
print(msg3.swapcase())

# Checking string is lower or upper with islower() and isupper()

msg1 = "My name is Yogeswar reddy"
print("Checking string is lower: ", msg1.islower())
print("Checking string is upper: ", msg1.isupper())
msg = "YOGESWAR"
print("Checking string is lower: ", msg.islower())
print("Checking string is upper: ", msg.isupper())

# convert string into lower or upper using lower() and upper()

msg = "My name is Yogeswar Reddy"
print("convert string into lower: ", msg.lower())
print("convert string into upper: ", msg.upper())

# Using function check given string is upper or lower
msg = "My name is Yogeswar reddy"
def is_upper_lower(msg1):
    if msg.isupper():
        return "UPPER CASE"
    elif msg.islower():
        return "lower case"
    else:
        return "Mixed Case"

print("The given string is: ", is_upper_lower(msg))
"""
Input : string = 'My Name is YOGESWAR from Anantapur'
Output : Uppercase - 11
         Lowercase - 18
         spaces - 5
         gEEKSFORGEEKS IS A COMPUTER sCIENCE PORTAL FOR gEEKS
"""
"""Algorithm
1. Traverse the given string character by character upto its length, check if character is in lowercase or uppercase using built in methods.
2. If lowercase, increment its respective counter, convert it to uppercase using upper() function and add it to a new string, if uppercase, increment its respective counter, convert it to lowercase using lower() function and add it to the new string.
3. If space, increment its respective counter and add it to a new string
4. Print the new string.
"""

string = "My Name is YOGESWAR from Anantapur"
new_string = ""
count1 = 0
count2 = 0
count3 = 0

for i in string:
    if i.isupper():
        count1 += 1
        new_string += (i.lower())
    elif i.islower():
        count2 += 1
        new_string += (i.upper())
    elif i.isspace():
        count3 += 1
        new_string += i

print("In original String : ")
print("Uppercase -", count1)
print("Lowercase -", count2)
print("Spaces -", count3)

print("After changing cases:")
print(new_string)