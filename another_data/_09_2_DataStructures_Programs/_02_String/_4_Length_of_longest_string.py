list1 = ["python", "programming", "yogeswar", "reddy"]

# Using built in function
res = max(list1, key= len)
print("Maximum length of string in list1: ", res)

max_len = -1
for elem in list1:
    if len(elem) > max_len:
        max_len = len(elem)
        res = elem
print(res)
# using algorithm

def longest_string():
    list1 = ["python", "programming", "yogeswar", "reddy"]
    max_len = -1
    for elem in list1:
        if len(elem) > max_len:
            max_len = len(elem)
            res = elem
print(res)

longest_string()