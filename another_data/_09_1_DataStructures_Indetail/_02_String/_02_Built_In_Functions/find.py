""" find() with no start and end arguments """
msg = "Let it be, let it be, let it be"

# find occurence of a sub string 'let it'
result = msg.find("let it")
print("Substring 'let it'  search in msg: ", result)
"""Conclusion : With the Find function we can find the position of the substring in string .
It means it shows start index of the sub string"""

# find occurence of sub string 'small'
result = msg.find("small")
print("Substring 'small'  search in msg: ", result)
""" Conclusion : If sub string is not found in string the output shows '-1' """

# use find() with if else
if msg.find("be,") != -1:
    print("Contains substring 'be,'")
else:
    print("Does not contain substring")

"""find() with start and end arguments"""

msg1 = "Sunrisers hyderabad won the match by 15 runs"

# Substring is searched in string with index starting from 12
print("substring is searched from 5: ", msg1.find("hyderabad", 12))
"""Conclusion : Substring searching from 'derabad' so the output is -1 
because substring not available from 12th position """

print("substring is searched from 5: ", msg1.find("hyderabad", 5))  # It starts from 10th poistion

print("substring is searched from 10 to -1 : ", msg1.find("won the match", 10, -1))  # it's starts from 20th position
print("substring is searched from -25 to -5 : ", msg1.find("match by", -25, -5))  # it's starts from 28th position
print("substring is searched from -25 to -10 : ", msg1.find("match by", -25, -10))  # it's not find between -25to-10
print("substring is searched from 15 to 45 : ", msg1.find("match by", 15, 45))  # it's starts from 28th position

""" Conclusion : Find() returns the number in the output it means sub string search in string and
 if it is there it shows index from starting otherwise it simply shows -1as result """