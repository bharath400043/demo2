msg1 = "python program"
print("---Message1----", msg1)
print("Variable type of msg1", type(msg1), "and Memory address of msg1:", id(msg1))

msg2 = "WELCOME YOGESH"
print("--- Message2---", msg2)
print("Variable type of msg2", type(msg2), "and Memory address of msg2:", id(msg2))

"""
STRING OPERATIONS:
1.Indexing
2.Slicing
3.Adding
4.Multiplying (but multiply a string with a number not a string)
5.Membership """

# Indexing:
print("Positive Indexing in msg1: ", msg1[3], msg1[9])
print("Negative Indexing in msg1: ", msg1[-9], msg1[-3])

# Slicing:
print("Slicing positive : ", msg1[5:11])  # print from index 6 to position 11
print("Slicing Negative : ", msg1[-6:-1])  #
print("Slicing with start stop step : ", msg2[0:13:1], "==", msg2[0:13], "==", msg2[0:13:2], "==", msg2[0:13:3])
print("Slicing without any positions + :", msg2[::], "==", msg2[2::], "==", msg2[:8:], "==", msg2[::2], "==", msg2[::3])
print("Slicing without any positions - :", msg2[::], "==", msg2[-2::], "==", msg2[:-8:], "==",
      msg2[::-2], "==", msg2[::-3], "==", msg2[-2::1])

# Adding
final_message = msg1 + msg2
print("Concatenation of strings : ", final_message)

# Multiplication
print("multiplication a string with number : ", msg1*3)
print("multiplication a string with number : ", final_message*0)

# Checking for Membership
print("---Membership---: ", "YOGESH" in msg2)
print("---Membership---: ", "python" not in msg1)


# CRUD Operations:
name = "yogeswar"  # Create

# Retrival
for each in name:
      print(each)
print("retrive 4th position letter : ", name[5])

# Update
# name[5] = "h"  TypeError: 'str' object does not support item assignment
print("retrive 4th position letter after update : ", name[5])

# Delete
# del name[5] TypeError: 'str' object doesn't support item deletion
del name