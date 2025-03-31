x = 33
y = 45
print("-------Logical and operator---------")
print("1.Logical and operator : ", x >= 10 and y > 5)
print("2.Logical and operator : ", x > 5 and y < 10)
print("3.Logical and operator : ", 0 and None)  # 0
print("4.Logical and operator : ", None and None)  # None
print("5.Logical and operator : ", None and 0)  # None
print("6.Logical and operator : ", 0 and 0)  # 0
print("7.Logical and operator : ", x < 5 and 0)
print("8.Logical and operator : ", x < 5 and y == 10)
print("9.Logical and operator : ", None and y > 5)  # None
print("10.Logical and operator : ", x >= 10 and None)  # None
print("11.Logical and operator : ", 0 and y > 5)  # 0
print("12.Logical and operator : ", x >= 10 and 0)  # 0
print("13.Logical and operator : ", 1 and y > 5)  # True
print("14.Logical and operator : ", 1 and 1)  # 1

print("-------Logical or operator-------")
print("1.Logical or operator : ", x > 5 or None)
print("2.Logical or operator : ", x >= 10 or y > 5)
print("3.Logical or operator : ", x > 5 or y < 10)
print("4.Logical or operator : ", 0 or None)  # None
print("5.Logical or operator : ", None or None)  # None
print("6.Logical or operator : ", None or 0)  # 0
print("7.Logical or operator : ", 0 or 0)  # 0
print("8.Logical or operator : ", x < 5 or 0)  # 0
print("9.Logical or operator : ", x < 5 or y == 10)
print("10.Logical or operator : ", None or y > 5)
print("11.Logical or operator : ", x >= 10 or None)
print("12.Logical or operator : ", 0 or y > 5)
print("13.Logical or operator : ", x >= 10 or 0)
print("14.Logical or operator : ", x < 5 or 1)  # 1

print("-------Logical not operator-------")
print(" Logical not operator : ", x is not 10)
print(" Logical not operator : ", y is not 45)
print(" Logical not operator : ", x is not 0)
