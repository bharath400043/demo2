
# STATE  : builtin data types
#             numbers (int float long complex)
#             string list tuple dict set
# Behavior : functions id() input() len() max() min()
#                      print()  type()
#                      int() float() long() str() list() tuple() dict() set()
list1 = [1, 2, 3, 4]
print(list1, type(list1), id(list1))
x = 10
list1.append(10)

import random
print("Random number : ", random.randint(1,100))

from random import randint
print("Random number : ", randint(1,100))

'''
sum(10,20)  # function calling
print(sum(10,20))
res = sum(10,20)
print("Result :",res)
'''
# Generate a random number between 1 to 100



'''
#include<stdio.h>
void main(){
    printf("Hello world")
}

.c ----> .obj 
3          503
'''

def sum(n1,n2):
    res = n1+n2
    return res


def sum(n1):
    res = n1
    return res

print(sum(10))

list1 = [1,2,3]
list1.append(100)


import random   # Here random is a module(in windows file)

print("Hello world ")  # 2 lines       Wrong -> 769 + 1
print("Random number : ",random.randint(1,100))   #173 line

'''
module  : .py file ,which contains colleciton of functions and classes   161 modules
package : folder, group of packages+modules   31 packages  

Folder : either only folders/only files/files+folders
'''

import collections
x = collections.OrderedDict
print("Ordered dict : ",x)


import concurrent.futures.process
import xml.dom.domreg
print("Print given list : ",xml.dom.domreg.well_known_implementations)


from random import randint,LOG4    # print(10)
print("Random number : ",randint(1,100))
print("Random number : ",LOG4)

# import vs from
import random     #  x = 10   print(x)
print("Random number : ",random.randint(1,100))
print("All functions : ",random.__all__)
print("Other attributres  :",random.LOG4,random.RECIP_BPF)



from _04_Operators._1_Arithmetic  import programs
print("From arithmetic : ",programs.xx)
print("From arithmetic : ",programs.yy)
print("From arithmetic : ",programs.zz)
print("From arithmetic : ",programs.aa)



#from _04_Operators._01_Arithmetic.programs import xx
#print("From arithmetic : ",xx)