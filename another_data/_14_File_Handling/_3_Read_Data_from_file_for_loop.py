

#my_file = open("C:/Users/madhu/Desktop/python_data.txt", 'r')
my_file = open("test.txt", 'r')
print(type(my_file))
print("----------------------")
'''
# Read data from file
for each_line in my_file:
    words = each_line.split()
    print(words)
'''
'''   
# Read data from file
for each_line in my_file:
    if 'Python' in each_line.split():
        print("YES, Python Word exists in this line")
    else:
        print("No keyword called Python in this line")
'''


# Using with statement
print("----Using with statement------")
#my_file = open("C:/Users/madhu/Desktop/python_data.txt", 'r')
with open("C:/Users/madhu/Desktop/python_data.txt", 'r') as my_file:
    print('--File type----',type(my_file))
    for each_line in my_file:
        words = each_line.split()
        print(words)
