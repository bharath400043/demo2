tup = (10, 15, 20, 25, 30, "yogi", ["python", -30.1], (25.2, 60))
print("Tuple ---- : ", tup)
# len()
print("Length of the tuple : ", len(tup))

# max()
# print("Maxvalue of the tuple : ", max(tup))   TypeError: '>' not supported between instances of 'str' and 'int'
tup1 = (10, 15, 50, -30.6, 70, 90.26, 10.0, 15, 25)
print("Tuple ---- : ", tup1)
print("Maxvalue of the tuple : ", max(tup1))

# min()
print("Minvalue of the tuple : ", min(tup1))

# count()
print("Count of 10 in tup : ", tup1.count(10))
print("Count of 15.0 in tup : ", tup1.count(15.0))
print("Count of -30.6 in tup : ", tup1.count(-30.6))
# tuple()
tup2 = tuple("programming")
print("--tuple ---", tup2)
# index()
print("Index of 10 in tup : ", tup1.index(10))
print("Index of 90.26 in tup : ", tup1.index(90.26))
print("Index of r in tup : ", tup2.index("r"))
print("Index of a in tup : ", tup2.index("a"))

# index() with star and end arguments
# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'o' after the 3th index is searched
index = alphabets.index('o', 3)   # 6
print('The index of o:', index)

# 'i' between 3rd and 7th index is searched
index = alphabets.index('i', 3, 7)
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
# print('The index of i:', index)


# sorted
print("Tuple ---- : ", tup)
# print("sorting of tuple :", sorted(tup))  TypeError: '<' not supported between instances of 'str' and 'int'
print("Tuple ---- : ", tup1)
print("sorting of tuple :", sorted(tup1))
print("reverse sorting of tuple :", sorted(tup1, reverse=True))
print("Tuple ---- : ", tup2)
print("sorting of tuple :", sorted(tup2))
print("reverse sorting of tuple :", sorted(tup2, reverse=True))

emp = ((10, "abc", 55000), (20, "reddy", 60000), (30, "pqr", 750000))
print("sorting based on name :", sorted(emp, key = lambda x: x[1]))
