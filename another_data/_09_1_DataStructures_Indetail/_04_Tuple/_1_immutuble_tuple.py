# Homogeneous,Heterogeneous
# Unique data,duplicate data
# ordered
# sequence
# Immutable
list1 = [1, 5, 6, "yogi", (1, 2, 3)]
# CRUD Operations
# Create and Retrieve
tup1 = ()
print("empty tuple: ", tup1)

tup1 = tuple()
print("empty tuple: ", tup1)
tup = (50)
print("---tup--", tup)

tup1 = (50,)
print("---Tuple---: ", tup1)

tup1_1 = tuple("programming")
print("---Tuple---: ", tup1_1)
tup1_1 = tuple([50, 20, 35])
print("---Tuple using tuple function of list---: ", tup1_1)
tup1_2 = 50, 60, 70
print("---Tuple with out using parentheses---: ", tup1_2)   # this is known as tuple packing
tup2 = (30, 25.2, "yogesh", ["python", "program"], (20, 30), (), 30)
print("---Tuple---: ", tup2, "Type :", type(tup2), "--id--: ", id(tup2))
# Retrieve
print("Retrieving---tup2[2]: ", tup2[2])
print("Retrieving---tup2[3][0]: ", tup2[3][0])
print("---loop---")
for each in tup2[3]:
    print(each)
for each in tup2:
    print(each)

# Update:
print("---Tuple---: ", tup2)
# tup2[2] = "reddy"     TypeError: 'tuple' object does not support item assignment
# tup2 = tup2 + "pqr"  TypeError: can only concatenate tuple (not "str") to tuple
# tup2 = tup2 + 50    TypeError: can only concatenate tuple (not "int") to tuple
# tup2 = tup2 + [50]   TypeError: can only concatenate tuple (not "list") to tuple
tup2 = tup2 + ("pqr",)
tup2 = tup2 + (50,)
tup2 = tup2 + ([2, 3, "yogi"],)
print("---Tuple After Update--: ", tup2)
tup2[3][1] = "welcome"
print("---Tuple After Update--: ", tup2)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Delete
print("---Tuple---: ", tup2, tup1)
# del tup2[3]   TypeError: 'tuple' object doesn't support item deletion
del tup1
# print(tup1)   Its shows error because already deleted
