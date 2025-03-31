"""index() is an inbuilt function in Python,
which searches for a given element from the start of the list and returns the lowest index where the element appears.
 *Returns lowest index where the element appears.
 *If any element which is not present is searched,it returns a ValueError
 *The index() method is almost the same as the find() method,
   the only difference is that the find() method returns -1 if the value is not found"""

"""Syntax:  str.index(substr, beg = 0 end = len(string))
*substr − This specifies the string to be searched whose lowest index will be returned.
*beg − This is the starting index, by default its 0.
*end − This is the ending index, by default its equal to the length of the string."""

# index() with substring argument only
msg = "Learn python programming is better"

result = msg.index("is better")
print("Substring 'is better' is searching in msg: ", result)
# result = msg.index("java")
# print("Substring 'java' is searching in msg: ", result)  "IT SHOWS VALUE ERROR"

# index() with start and end argments
msg = "Learn python programming is better"
print("substring 'programming' is searched from 10: ", msg.index("programming", 10))
print("substring 'is bet' is searched from 15 to -2: ", msg.index("is bet", 15, -2))
print("substring 'programming' is searched from -25 to -1: ", msg.index("programming", -25, -1))
# print("substring 'programming' is searched from 0 to 10: ", msg.index("programming", 0, 10)) "VALUE ERROR'


