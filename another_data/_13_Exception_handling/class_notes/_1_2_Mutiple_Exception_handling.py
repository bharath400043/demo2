'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_1_Exception_handling.py", line 6, in <module>
    print("Division :", x / y)
ZeroDivisionError: division by zero
'''
print("Start of program")
try:
    print("----While Exception handling----")
    x = int(input("Enter numerator value :"))
    y = int(input("Enter denominator value:"))
    print("Division :", x / y)
    print("Hello world")
    print("---------------------------------")
except ValueError as ve:
    print("** Please enter numbers for num/den values **")
    # print(ve)
except ZeroDivisionError as zde:
    print("** Please enter den. value other than 0 **",zde)


print("End of program")  #remaining piece of code
'''
Exception didn't happen :  1. Statements before try block
                           2. Statements in try block(ALL)
                           3. Statements after except block
                           
Exception occured       :  1. Statements before try block
                           2. Statements in try block,till the line of exception occurance
                           3. Statements in except block
                           4. Statements after except block     
                           
 - Python at a time,handles only one exception
 - If there is chance of mulitiple exceptions,handle using multiple except blocks
 -                 
'''

