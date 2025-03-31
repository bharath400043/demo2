# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)

product(3,4)

# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)
# This line will call the second product method
product(3,4)
product(4, 5, 5)