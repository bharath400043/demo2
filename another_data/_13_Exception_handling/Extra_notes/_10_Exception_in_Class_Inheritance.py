'''
@author: madhu
'''

class A(Exception):
    pass
class B(A):
    pass
class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls() # raise A() raise B() raise C()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")
        
print("----------")

class X(Exception):
    pass
class Y(X):
    pass
class Z(Y):
    pass

for cls in [X,Y,Z]:
    try:
        raise cls()
    except Z:         # Exception
        print("Z")
    except Y:         # ArithmeticError
        print("Y")
    except X:
        print("X")    # ZeroDivisionError
    
    
    '''
    except X:         # Exception
        print("X")
    except Y:         # ArithmeticError
        print("Y")
    except Z:
        print("Z")    # ZeroDivisionError
    '''
