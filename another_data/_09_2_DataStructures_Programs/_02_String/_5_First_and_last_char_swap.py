str1 = "yogeswar"

print("before swap: ", str1)
print("after swap: ", str1[-1] + str1[1:-1] + str1[0])
"""
myString = "yogeswar"
newString = (myString[1:len(myString)-1])
newString[0] = myString[len(myString)-1]
newString[len(newString)-1] = myString[0]
print(newString)
"""

msg = "python"
list1 = list(msg)
list1[0], list1[-1] = list1[-1], list1[0]
msg = ''.join(list1)
print(msg)

mystr = "program"
mylist = list(mystr)
store = mylist[0], mylist[-1]
mylist[0] = store[1]
mylist[-1] = store[0]
print(''.join(mylist))
