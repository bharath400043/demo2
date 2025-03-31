print("--- assign int and float  values to variable by all operations ----")
x = 50

x += 5
print("Update x value by assigning 5 by addition: ", x)

x -= 10
print("Update x value by assigning 10 by substraction: ", x)

x *= 3
print("Update x value by assigning 3 by multiply: ", x)

x /= 5
print("Update x value by assigning 5 by division: ", x)

x %= 2
print("Update x value by assigning 2 by modulus: ", x)

y = 95

y //= 3.0
print("Update y value by assigning 3.0 by floordivision: ", y)

y **= 2
print("Update x value by assigning 2 by exponent: ", y)

print("--- assign num to a string values to variable by all operations ----")

name = "yogesh"

# name += 15
# print("Update name by assigning 15 by addition: ", name)

name *= 4
print("Update name by assigning 4 by multiply: ", name)

""" Conclusion: We already know that We can not assign string to a number by perform Arithmetic operations 
except multiplication operation """

print("--- assign string  to a string values to variable by all operations ----")

company = "TCS"

company += "employee"
print("Update company by assigning 'employee' by addition: ", company)

# company -= "salary"
# print("Update company by assigning 'salary ' by substraction: ", company)
""" Conclusion : As we know We can not assign a string to string by perform Arithmetic operations 
except Addition operation"""
