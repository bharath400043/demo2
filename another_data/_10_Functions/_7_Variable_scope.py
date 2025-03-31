"""
1.Local variables --> These variables we can use or access only with in/inside the function. we can't access outside of the function
2.Global variables -->Thsese varibles we can access all over the program where ever we want we can access and have widest accessibility
"""
x = 100   # Global variable
print(x)
def getdata():
    x = 20   # Local variable we can access with in the function only
    print(x)
getdata()
print(x)

