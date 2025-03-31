
def mult(x):
    return x*10  # single line expression  x*x x*x*x    x**x

print(mult(15))

print("----------Ananymous function-----------")
val = lambda x : x*10
print(val(15))


def get_pow(x,y):
    return x ** y
print(get_pow(10,5))

pow = lambda x,y : x ** y
print(pow(10,5))

def get_moduls(x, y):
    return x % y
print("modulus: ", get_moduls(60, 8))

modulus = lambda x, y: x % y
print("modulus using lambda: ", modulus(60, 8))

