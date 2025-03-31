tup1 = (5, 20.5, "yogi", -30.1, ["python", "programming"], (20, 35), (50), ())
print("---Tuple---: ", tup1)

# Indexing
print("---Indexing---")
print("tup1[2]: ", tup1[2])
print("tup1[3]: ", tup1[3])
print("tup1[-2]: ", tup1[-2])
print("tup1[-6]: ", tup1[-6])
print("tup[:]: ", tup1[:])
print("tup[4][1]: ", tup1[4][1])
print("tup[5][0]: ", tup1[5][0])
print("tup[-4][-2]: ", tup1[-4][-2])

# Slicing:
print("---Tuple---: ", tup1)
print("----Slicing----")
print("tup[:]: ", tup1[:])
print("tup[0:]: ", tup1[0:])
print("tup[:7]: ", tup1[:7])
print("tup[3:6]: ", tup1[3:6])
print("tup[::2]: ", tup1[::2])
print("tup[1:7:2]: ", tup1[1:7:2])
print("tup[4][:]: ", tup1[4][:])
print("tup[5][:-1]: ", tup1[5][:-1])
print("tup[-4][0:2]: ", tup1[-4][0:1])

print("tup[-1:]: ", tup1[-1:])
print("tup[:-1]: ", tup1[:-1])
print("tup[-3:]: ", tup1[-3:])
print("tup[-1:-6]: ", tup1[-1:-6])
print("tup[-6:-1]: ", tup1[-6:-1])
print("tup[-6:-1:2]: ", tup1[-6:-1:2])
print("tup[-6:-1:-2]: ", tup1[-6:-1:-2])
print("tup1[3:-2]: ", tup1[3:-2])
print("tup1[3:-2:2]: ", tup1[3:-2:2])

# Adding annd Multiplying
student = (10, "yogi", 50, 60, 70, 80, 90)
rno, name = student[0:2]
print("rank no: ", rno)
print("name of student : ", name)
fees = (25000,) * 4  # Multiplying
print("fees : ", fees)

student1 = student + fees   # We can add both tuples but it returns a new tuple
print("student1: ", student1)

tup2 = (10, "yogesh", [30, 25])
print("---tup2---",tup2)
tup2 = tup2 * 3
print("after Multiplying Tuple ---", tup2)

# Membership
print("---Tuple---: ", tup1)
print("Checking membership: ", 20.5 in tup1)
print("Checking membership: ", "python" in tup1)  # False because it is in list in tup1
print("Checking membership: ", 35 in tup1)   # False because it is in tup in tup
print("Checking membership: ", () in tup1)
print("Checking membership: ", 50 not in tup1)
