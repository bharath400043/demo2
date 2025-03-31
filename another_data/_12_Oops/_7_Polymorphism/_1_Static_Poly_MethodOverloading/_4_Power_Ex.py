'''
Created on 20-Jun-2017
@author: yugan
'''

def get_power(voltage, state='state', action='action', type='type'):
    print ("VOLTAGE = ", voltage)
    print ("STATE   = ", state)
    print ("ACTION  = ", action)
    print ("TYPE    = ", type)
    print("---------------End of method--------------")

'''
get_power()                         # required argument missing
get_power(voltage=5.0, 'dead')      # non-keyword argument after a keyword argument
get_power(110, voltage=220)         # duplicate value for the same argument
get_power(110,actor='John Cleese')  # unknown keyword argument
'''

print("--------# 1 positional argument----------")
get_power(1000)
get_power(1000,'X')
get_power(1000,'X','Y')
get_power(1000,'X','Y','Z')

print("------------------# 2 keyword argument------------------------")
get_power(action="myaction", type="mytype", voltage=1000)  # 2 keyword argument

print("------------------------------------------")
get_power(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments

print("------------------------------------------")
get_power(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
print("------------------------------------------")

get_power('a million', 'brief of life', 'jump')            # 3 positional arguments
print("------------------------------------------")

get_power(1000, action='pushing up the daisies')           # 1 positional, 1 keyword
print("------------------------------------------")

