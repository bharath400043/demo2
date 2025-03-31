msg = "yoges\nwar reddy\n"

def remove_newline(msg):
    res = msg.replace("\n", "")
    print(res)

remove_newline(msg)

list1 = ["stri\nke", "slo\nw", "bo\nwl"]

for i in list1:
    res = i.replace("\n", "")
    print("after removing newline: ", res)

res = []
for i in list1:
    res.append(i.replace("\n", ""))
print("after removing newline: ", res)

print('test string\n'.rstrip())
print('test string \n \r\n\n\r \n\n'.rstrip())

s = "   \n\r\n  \n  abc   def \n\r\n  \n  "
print(s.strip())