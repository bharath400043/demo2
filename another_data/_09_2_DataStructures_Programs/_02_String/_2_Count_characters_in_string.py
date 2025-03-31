'''
Requirement :  Count characters in string
1. Categorize req,input data parts
2. C R U D
3. Datatype
4. State, Behavior

Requirement : Count characters in string

Step 1:  Input data   : given string
         Req(Question): Find count of a char in string
Step 2:  Retrieval    : We are getting count of a character
Step 3:  Datatype     : String :
Step 4:  State :
         Behavior:
'''
string1 = "python programming"
print(string1.count("p"))
check = input("enter you want to check count: ")
def char_count_in_string():
    count = 0
    for i in string1:
        if i == check:
            count += 1
    return count
print(char_count_in_string())