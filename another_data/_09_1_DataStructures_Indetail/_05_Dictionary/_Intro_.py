"""
Dictionary :
* Key -value pair -->items
* keys should be unique and immutable
* value will be any type of datatype nad mutable or immutable also
C R U D Operations

"""
# Ceate
dict1 = {}
print("Dictionary: ", dict1)
dict1["name"] = "yogi"
dict1["location"] = "Anantapur"
print("Dictionary: ", dict1)

dict1 = {1: 100,
         3.5: "float",
         "name": "yogi",
         (1, 2, 3): [4, 5, "yash"],
         "bng": True,
         "data": {100, 25000}}
print("Dictionary1: ", dict1)
val = str(dict1)
print("String format: ", val, type(val))
val1 = list(dict1)
print("List format: ", val1, type(val1))
list1 = [1, 2.3, "yogi", (4, 5), "id"]
list2 = ["hi", "float", "name", "tup", 195]
dict0 = dict.fromkeys(list1, list2)
print(dict0)
dict0 = dict.fromkeys(list1, 10)
print(dict0)
print("----create dictionary----")
emp_data = {"name": "Yogesh",
            "id": 195,
            "desn": "Python developer",
            "loc": "Bangalore"
            }
print("emp_data : ", emp_data)

# Retrieve
print("----Retrieve----")
print("emp_data['desn']: ", emp_data["desn"])
# print("emp_data['adress']: ", emp_data["adress"])   KeyError

# Update
print("----Update----")
emp_data["loc"] = "Hyderabad"
print("emp_data['loc']: ", emp_data["loc"])
emp_data["salary"] = 15000  # Add New Entry
print("emp_data['salary']: ", emp_data["salary"])
print("emp_data : ", emp_data)

# Delete
del emp_data["loc"]
print("emp_data : ", emp_data)
emp_data.clear()
print("emp_data : ", emp_data)
del emp_data
# print("emp_data : ", emp_data)  # Already dict deleted
