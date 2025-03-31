x = 40
y = 15

print("sum : ", x+y)
print("substraction : ", x-y)
print("multiplication : ", x*y)
print("division : ", x/y)
print("modulus : ", x % y)
print("exponential : ", x**y)
print("floordivision : ", x//y)

print("-----******------")
x = 6
y = "yogesh"  # string

print("multiplication : ", x*y)
# print("sum : ", x+y)
# print("substraction : ", x-y)
# print("division : ", x/y)
# print("modulus : ", x%y)
# print("exponential : ", x**y)
# print("floordivision : ", x//y)

""" Conclusion: We can not perform Arithmetic operations for a string and a int or float value 
except multiplication operation """

print("-----******------")
x = 23.15  # float
y = 13

print("sum : ", x+y)
print("substraction : ", x-y)
print("multiplication : ", x*y)
print("division : ", x/y)
print("modulus : ", x % y)
print("exponential : ", x**y)
print("floordivision : ", x//y)

""" Arithmetic op[ertaions on two strings """
emp_name = "yogesh"
company = "TCS"

print("sum : ", emp_name+company)
# print("substraction : ", emp_name-company)
# print("multiplication : ", emp_name*company)
# print("division : ", emp_name/company)
# print("modulus : ", emp_name % company)
# print("exponential : ", emp_name**company)
# print("floordivision : ", emp_name//company)

""" Conclusion : We can not perform Arithmetic operations on both strings except Addition operation"""

""" Requirement : Calculator for  years into days , hours, minutes and seconds """

print("---- Calculator for  years into days , hours, minutes and seconds----")

num_years = int(input("enter No. of years to converts seconds : "))
days_in_year = 365
hours_in_day = 24
min_in_hour = 60
sec_in_min = 60

print("Convert years into days : ", num_years * days_in_year)
print("Convert years into hours : ", num_years * days_in_year * hours_in_day)
print("Convert years into minutres : ", num_years * days_in_year * hours_in_day * min_in_hour)
print("Convert years into seconds : ", num_years * days_in_year * hours_in_day * min_in_hour * sec_in_min)
