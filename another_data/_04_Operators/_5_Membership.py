x = [1, 5, 12, 18, 20, 25]

print(" check 5 is in list or not : ", 5 in x)
print(" check 6 is in list or not : ", 6 in x)

print(" check 12 is in list or not : ", 12 not in x)
print(" check 2 is in list or not : ", 2 not in x)

list1 = [20, 15, "yogesh", ["hello", 60, "python"], "world"]

print(" check 60 is in list or not : ", 60 in list1)
print(" check world is in list or not : ", "world" in list1)
print(" check hello is in list or not : ", "hello" in list1)
print(" check hello, 60, python is in list or not : ", ["hello", 60, "python"] in list1)
print(" check 60 is in list or not : ", 60 not in list1)

""" Conclusion : when we check membership in list of list that inner list consider as an element for a outer list
when we check membership for a single element in inner list it shows false and check entire inner list then it shows true"""

set1 = {25,3,56.32,9,25}
print(" check 25 is in set or not : ", 25 in set1)
print(" check 56.32 is in set or not : ", 56.32 in set1)

dict1 = {"names" : ["yogesh", "swaroop"],
         "company" : ["TCS", "HCL"]}
print(dict1)
print(" check TCS is in dict or not : ", "TCS" in dict1)
print(" check names is in dict or not : ", "names" in dict1)
print(" check name is in dict or not : ", "swaroop" in dict1)

""" Conclusion : same as list"""

