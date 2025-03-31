# https://www.geeksforgeeks.org/args-kwargs-python/
# *ARGS
print("----Program 1 -------------")
def myFun(*args):
    print(args,type(args))
    for arg in args:
        print(arg)
    print("*******")

myFun()
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
myFun(1,2,3,4,5)
myFun(1,2.4,'Madhu',True,[1,2,3],(1,2,3),{1:1,2:2},{11,2,3})

x = 'Madhu'
print("My name is ",x)
print("Hello")

print("-------Program 2----------------")
def myFun(val, *args):
    print("First argument :", val)
    for arg in args:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("================ KWARGS ==================")

def myFun(**kwargs):
    print(kwargs,type(kwargs))
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

print("---------Program2 --------------")
def myFun(val, **kwargs):
    print("First parameter : ",val)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun("Hi", first='Geeks', mid='for', last='Geeks')

print("----Program 2---------")
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)  #myFun("Geeks", "for", "Geeks")

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


print("--------------For Decorator purpose-----------")
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("------------")


# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun()


myFun('geeks', 'for','geeks', first="Geeks", mid="for", last="Geeks")
myFun('geeks', 'for', 'geeks', {1:1,2:2,3:3})
print("----Default function call-----")
