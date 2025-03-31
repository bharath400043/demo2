emp_data = {"name": "Yogesh",
            "batch": 13,
            "id": 195,
            "desn": "Python developer",
            "loc": "Bangalore"
            }
print("emp_data : ", emp_data)
# Len()
print("Length of dict: ", len(emp_data))
print("Maximum of dict: ", max(emp_data))  # based on alphabet of keys

# Keys()
print("keys from emp_data : ", emp_data.keys())
# Values
print("values from emp_data : ", emp_data.values())
# Items
print("items from emp_data : ", emp_data.items())
# Update
dict1 = {"salary": 15000,
         (1, 2, 3): [4, 5, 6]}

emp_data.update(dict1)
print("dict1: ", dict1)
print("---Updated dictionary: ", emp_data)

# clear
print("dict1: ", dict1)
dict1.clear()
print("dict1 after clear(): ", dict1)

# fromkeys()
list1 = [1, 2.3, "yogi", (4, 5), "id"]
list2 = ["hi", "float", "name", "tup", 195]
dict0 = dict.fromkeys(list1)
print(dict0)
dict0 = dict.fromkeys(list1, list2)
print(dict0)
dict0 = dict.fromkeys(list1, 10)
print(dict0)

# copy()
print("dict0: ", dict0)
dict2 = dict0.copy()
print("dict2: ", dict2)

# in (Membership) (has_key)
print("name in emp_data :", "name" in emp_data)
print("yogesh in emp_data :", "Yogesh" in emp_data)  # False because it doesn't find values

# get(Key)  get(key, default = None)
print("---Updated dictionary: ", emp_data)
print("id in emp_data: ", emp_data.get("id"))
print("age in emp_data : ", emp_data.get("age"))  # if the key is not available in dict then value come default None

# setdefault()
emp_data.setdefault("age", 23)
print("---Updated dictionary: ", emp_data)
