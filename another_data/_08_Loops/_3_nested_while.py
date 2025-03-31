""" Requirement : Finding prime numbers with nested while """
print("----prime numbers ----")
i = 2
while i < 50:
    j = 2
    while (j <= (i/j)):
        if not (i % j):
            break
        j += 1
        if (j > i/j):
            print(i, " is a prime number")
    i += 1
print("good bye")