# CRUD
# Datatype
"""Basic Operations in List:
1.Indexing
2.Slicing
3.Adding
4.Multiplying
5.Membership
"""

list1 = [5, 23.2, "yogi", True, {"role": "developer"}, (1, 2, 3), ["python", "programming"]]

# Indexing
print("list1[3]: ", list1[3])  # Retrieve
print("list[-3]: ", list1[-3])
list1[3] = False
print("list1 after update: ", list1)   # we can update list with indexing
print("list1[-1][0]: ", list1[-1][0])
print("list1[-2][-2]: ", list1[-2][-2])

# Slicing

print("lis1[1:5]: ", list1[1:5])
print("lis1[:]: ", list1[:])
print("list1[-1:]:", list1[-1:])
print("list1[:-1]:", list1[:-1])
print("list1[-1:0]:", list1[-1:0])
print("list1[-1:-5]:", list1[-1:-5])
print("list1[-5:-1]:", list1[-5:-1])
print("list1[-5:-1:2]:", list1[-5:-1:2])
print("list1[-5:-1:-2]:", list1[-5:-1:-2])
print("lis1[1:5:2]: ", list1[1:5:2])
print("lis1[1:5:-2]: ", list1[1:5:-2])
print("lis1[::-2]: ", list1[::-2])

a = [1, 2]
b = [3, 4]
a[len(a):] = b
print("a: ", a)

# Adding
list2 = ["reddy", 20, (4, 5)]
list3 = list1 + list2          # Upadte
print("After adding 2 lists: ", list3)
list2.append(30)
print("list2: ", list2)   # after adding

# Multiplying
print("multiplyinng lits2 * 3 : ", list2 * 3)   # update
print("list1*-2: ", list1*-2)   # empty list

# Membership
print("list1: ", list1)
print("checking membership (1,2,3) in list1: ", (1, 2, 3) in list1)
print("Membership: ", "yogi" not in list1)