print("----------------Normal apporach---------------")
try:
    file_obj = open("C:/Users/madhu/Desktop/write_data1.txt", 'w')
    print("File type ", file_obj, type(file_obj))
    data = input("Enter text : ")
    file_obj.write(data) # TextIOWrapper.write(my_file,data)
except FileNotFoundError as fnf:
    print("File not found at specified path")
    print(fnf)
finally:
    # condition to check whether object my_file exists or not
    file_obj.close()
    
print("---Completed---")


print("----------------Using  functions---------------")
def write_data(file):
    try:
        file_obj = open(file, 'w')
        print("File type ", file_obj, type(file_obj))
        data = input("Enter text : ")
        file_obj.write(data)  # TextIOWrapper.write(my_file,data)
    except FileNotFoundError as fnf:
        print("File not found at specified path")
        print(fnf)
    finally:
        # condition to check whether object my_file exists or not
        file_obj.close()

    print("---Completed---")
file_path = "C:/Users/madhu/Desktop/write_data2.txt"
write_data(file_path)


print("----------------Using OOPs concepts---------------")
class FileHandling:
    def __init__(self,file_obj):
        self.file_obj = file_obj

    def write_data(self,in_data):
        try:
            file_obj = open(self.file_obj, 'w+')
            print("File type ", file_obj, type(file_obj))
            file_obj.write(in_data)  # TextIOWrapper.write(my_file,in_data)
        except FileNotFoundError as fnf:
            print("File not found at specified path")
            print(fnf)
        finally:
            # condition to check whether object my_file exists or not
            file_obj.close()

file_obj = FileHandling("C:/Users/madhu/Desktop/write_data3.txt")
data = 'Hello world. This is my third file'
file_obj.write_data(data)

'''
data = 'Hello world. This is my third file'
file_obj = FileHandling("C:/Users/madhu/Desktop/write_data3.txt",data)
file_obj.write_data()

file_obj = FileHandling()
file_obj.write_data(f_path,data)
'''