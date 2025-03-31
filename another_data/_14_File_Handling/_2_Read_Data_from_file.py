'''
'''

my_file = open("C:/Users/madhu/Desktop/write_data.txt", 'r')
# Read data from file
f_data = my_file.read() # File content will be store in string format
print("File content :",f_data)
print("After splitting :",f_data.split("\n"))
print("--------------")

# Check word count of  'REST'  in write_data.txt
counter = 0
for line in f_data.split("\n"):
    print(line)
    if "REST" in line:
        counter += 1
        print("**** :",line)

print("REST word repeated times in file : ",counter)

my_file.close()


print("----------Using functions---------")

def find_word_count(file,word):
    f_obj = open(file, 'r')
    f_data = f_obj.read()
    counter = 0
    for line in f_data.split("\n"):
        if word in line:
            counter += 1
            #print("**** :", line)

    print("REST word repeated times in file : ", counter)

f_name = "C:/Users/madhu/Desktop/write_data.txt"
s_word = input("Enter word to search : ")
find_word_count(f_name,s_word)

