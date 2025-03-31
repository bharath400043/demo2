fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("current fruit : ", fruit)
    for char in fruit:
        print("char in fruit : ", char)

""" Requirement : Find the prime numbers between 10 to 30 by using for loop and else statements"""

lower = 10
upper = 30
print("Prime numbers between {} and {} are: ".format(lower, upper))
for num in range(lower, upper+1):
    for i in range(2, num//2):
        if num % i == 0:
            break
    else:
        print("{} is a prime number".format(num))
