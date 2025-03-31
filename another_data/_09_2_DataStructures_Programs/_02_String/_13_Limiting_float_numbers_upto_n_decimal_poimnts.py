sal = 1500.43857

print("{:.2f}".format(sal))
print("printing upto 2 decimal points: {:.2f}".format(sal))
print("printing upto 3 decimal points: {:.3f}".format(sal))

x = round(sal, 2)
print(x)

x = 12.35874
print("{:12.2f}".format(x))   # It will print the value after 12 empty spaces in console

x = 12.35874
print("% 12.2f" % x)
