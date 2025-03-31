'''
Created on 18-May-2017

@author: yugan
'''

class MyClass(object):

    def __init__(self, data):
        self.mydata = []
        if isinstance(data, list):
            self.mydata=data
        elif isinstance(data, tuple):
            self.mydata = list(data)
            '''
            for i in data:
                self.mydata.append(i)
            '''
        else:
            self.mydata.append(data)

    def getData(self):
        print("Data is :",self.mydata)





li = MyClass( [1,2,3] )
li.getData()


tup = MyClass( (1,2,3) )
tup.getData()

num = MyClass(10)
num.getData()

dict1 = MyClass({'id':100,'name':'Madhu'})
dict1.getData()