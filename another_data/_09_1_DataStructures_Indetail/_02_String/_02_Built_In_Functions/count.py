msg = "my name is yogi"
sub = "i"

print("number of times substring repeats in string : ", msg.count("yogi"))
print("number of times substring repeats in string : ", msg.count(sub))
print("number of times substring repeats in string : ", msg.count(sub, 0, 11))
print("number of times substring repeats in string : ", msg.count(sub, 0, 15))

msg1 = "python is high level language and easy to read, learn and write"
sub1 = "read"

print("----{}----".format(msg1))
print("number of times substring repeats in string : ", msg1.count("yogi"))
print("number of times substring repeats in string 'and': ", msg1.count("and"))
print("number of times substring repeats in string 'and': ", msg1.count("and", 5, 15))
print("number of times substring repeats in string 'and': ", msg1.count("and", 20, 45))
print("number of times substring repeats in string 'python': ", msg1.count("python"))
print("number of times substring repeats in string 'python': ", msg1.count("python", 0))
print("number of times substring repeats in string 'python': ", msg1.count("thon", 10, 45))
print("number of times substring repeats in string : ", msg1.count(sub1))


msg2 = "welcome python"

print(msg2.count("python", 0, 20))
print(msg2.count("thon", -1, -20))
