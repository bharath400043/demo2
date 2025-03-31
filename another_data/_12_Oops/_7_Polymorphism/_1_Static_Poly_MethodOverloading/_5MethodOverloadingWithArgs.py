'''
Created on Aug 31, 2018
@author: mnettem
https://www.geeksforgeeks.org/python-method-overloading/
'''
# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype =='int':
        answer = 0
    # if datatype is str
    # initialize answer as ''
    if datatype =='str':
        answer =''
    # Traverse through the arguments
    print("----*args------",args)
    for x in args:
        # This will do addition if the 
        # arguments are int. Or concatenation 
        # if the arguments are str
        answer = answer + x
    print(answer)
 
 
# Integer
add('int', 5, 6,10,11,12,13,14)
# String
add('str', 'Hi ', 'Geeks',"Hello")