'''
Created on Dec 9, 2019
@author: madhu
'''

try:
    raise NameError("Getting Name Error")
except NameError as name:           # NameError name = NameError("Getting Name Error")
    print("AN EXCEPTION OCCURED ::",name)
