'''
Polymorphism:
-------------------
Static Polymorphism  - method overloading  - same class
Dynamic Polymorphism - method overriding  - super class,sub class (Inheritance)
'''

class FeedbackForm:

    def __init__(self):
        pass

    def feedback(self, rating = 5, comments = None):
        print("Feedback is :",rating,", ",comments)

    def get_data(self,*args,**kwargs):
        pass

# Method overloading
feed = FeedbackForm()
feed.feedback()
feed.feedback(10)
feed.feedback(9,'Good')
feed.feedback(comments ='Very Good')


#Function overloading
def sum(a=10, b=20, c=30):
    print("Sum is ", a+b+c)

# Overloading - Depends on how many arguments we are passing
sum()
sum(15)
sum(15, 25)
sum(b=200, a=100)
sum(b=200, c=300)
sum(a=100, c=300)
sum(b=200, a=100, c=300)



def add(x,y):
    pass

def sum(a,b):
    res = add(a,b)
