x = 10
print(x)
print("variable type :", type(x))
print("Memory location : ", id(x))

x = y = 30
print("Memory location : ", id(x))
print("Memory location : ", id(y))

x = y = 301
print("Memory location : ", id(x))
print("Memory location : ", id(y))


a = 555
print("Memory location : ", id(a))
b = 555
print("Memory location : ", id(b))
print(a == b)
print(a is b)

salary = 25581.45
print("Salary : ", salary, "and Variable type: ", type(salary))


a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyz"
print(type(a))
print("Memory location : ", id(a))
b = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyz"
print(type(b))
print("Memory location : ", id(b))

# List
student_marks = [50, 70, 80, 90]
print(student_marks)
print("Variable type : ", type(student_marks))
print(id(student_marks[0]))
print(id(student_marks[2]))

# Int
emp_count = 100
print("emp_count : ", emp_count, " and Variable type : ", type(emp_count))

# Float
distance = 6.0
print("Distance in KM : ", distance, "Variable type : ", type(distance))
salary = 15030.53
print("Salary : ", salary, "Variable type : ", type(salary))


# String
student_name = "Yogi"
print("Student Name : ", student_name, "Variable type : ", type(student_name))

print("----Assign same vallue to multible variables___")
a = b = c = 50
print(a)
print(b)
print(c)

# Unicode String
name = u"Yogesh@23.@#8"
print("Name : ", name, "Variable type : ", type(name))
