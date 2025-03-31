for letter in "python":
    print(letter)

fruits = ["banana", "apple", "mango"]
for index in range(len(fruits)):
    print("current fruit : ", fruits[index])
print("exit")

fruits = ["banana", "apple", "mango"]

for fruit in fruits:
    print(fruit)
print("---printing even numbers in range of 100 with interval 3")
for num in range(1,100,3):
    if num % 2 == 0:
        print(num, "Number is even")
    else:
        print(num, "Number is odd")
