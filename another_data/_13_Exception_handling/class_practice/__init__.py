# Name Error
try:
    length = 0
    for each in name:
        length += 1
    print("Length of given string: ", length)

except NameError as ne:
    print("please define name variable", ne)

# ImportError
try:
    from random import ranint
    random.randint(1, 20)
except ImportError:
    print("check the import module")

# TypeError
try:
    name = 1234
    length = 0
    for each in name:
        length += 1
    print("Length of given string: ", length)

except TypeError as te:
    print("please check variable type", te)


