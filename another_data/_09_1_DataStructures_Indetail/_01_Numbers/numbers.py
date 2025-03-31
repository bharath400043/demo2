# Datatypes
# Numbers : int float
# boolean : True False


x = 10
print(x, id(x), type(x))
x = 10.4
print(x, id(x), type(x))

x = 10.4
x = int(10.4)  # Data Loss Explicit casting
print(x)
x = 10
x = float(10)  # Promotion Implict casting
print(x)

is_active = True
print(is_active, id(is_active), type(is_active))

a = 32.05
print("absolute value of a : ", abs(a))
