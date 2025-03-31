count = 0
while count < 8:
    count += 1
    print("The count is : ", count)

i = 0
while i <= 8:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
print("end of loop")

print(" ------searching for an element in a list ----")
emp = ["yogi", "yashu", "swaroop", "ramu"]
name = "suresh"
i = 0
while i < len(emp):
    if emp[i] == name:
        break
    i += 1
else:
    print(name, "is not found in emp list")
