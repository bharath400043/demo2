x = y = 30
print(id(x))
print(id(y))
print(x == y)
print(x is y)

print("********")
a = 555
print(id(a))
b = 555
print(id(b))
print(a == b)
print(a is b)

print("********")
a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyz"
print(type(a))
print(id(a))
b = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" \
    "abcdefghijklmnopqrstuvwxyz"
print(type(b))
print(id(b))
print(a is b)
print(a is not b)

print("********")
x = 400
print(id(x))
y = 400
print(id(y))
print(x is y)

print("********")
x = "hello world"
y = "python"
print(x is y)
