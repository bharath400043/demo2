x = 10
print(x)   # print(x.__str__())
list1 = [1,2,3]
print(list1)

class Employee(object):
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __str__(self):  # method overriding
        content = str(self.eid)+" * "+self.name+" * "+str(self.sal)
        return content # implementing our own logic

madhu = Employee(1001,'MadhuN',10000)
print(madhu)  #print(madhu.__str__())






print("-------------------------")

class Employee(object):

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def get_emp_details(self):
            print("Employee Details are : ",self.id,self.name,self.sal)

    def __str__(self):  # method overriding
        content = str(self.id)+" * "+self.name+" * "+str(self.sal)
        return content # implementing our own logic

madhu = Employee(100,'MadhuN',4000)
madhu.get_emp_details()
print(madhu)
print("----------------------------------")
# madhu.__getattribute__()
print("Madhu hash val ",madhu.__hash__())
print("Madhu obj :",madhu)  # madhu.__str__()


'''
str vs repr
init vs new
object class in detail


'''