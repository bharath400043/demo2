# CRUD
# Datatype
# Create
list1 = [1, 5, 5.6, "yogi", 456, ["python", 22, "roop"]]   # Create
print("printing list1 : ", list1)
# Retrive
print("list1[3]:", list1[3])
print("list1[1:4]: ", list1[1:4])
print("list1[5][1]: ", list1[5][1])

# Updating
print("Befor update value at index 2 in list1: ", list1[2])
list1[2] = 195  # It erases old value and replace a new value
print("After update new value at index 2 in list1: ", list1[2])

print("printing list1 : ", list1)
# Delete
print("Before delete value at index 1 in list1: ", list1[1])
del list1[1]
print("After delete value at index 1 in list1: ", list1[1])
print("before delete printing list1 : ", list1)
del list1[4][1]
print("after delete printing list1 : ", list1)
del list1[4][1]
print("after delete printing list1 : ", list1)
