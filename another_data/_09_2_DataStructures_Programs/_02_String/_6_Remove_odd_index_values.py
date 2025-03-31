msg = "yogeswar reddy"

def remove_odd_index(msg):
    res = ''
    for i in range(len(msg)):
        if i % 2 == 0:
            res += msg[i]
    return res

print(remove_odd_index(msg))