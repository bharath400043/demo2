
'''
Update salary of employee based on rating.
5 - 50%  *
4 - 40%
3 - 15%  *
2 - 5%(Improve yourself)
1 - 0%(attend practice sessions) *
'''

'''
class Employee:

    def __init__(self,eid,name,sal,rating):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.rating = rating

    def update_hike(self):
        print("Emp details Before : ", self.eid, self.name, self.sal)
        if self.rating == 5:
            self.sal = self.sal + self.sal * 50 / 100
        elif self.rating == 3:
            self.sal = self.sal + self.sal * 15 / 100
        else:
            print(" No hike applicable for you.Improve yourself !!")

        print("Emp details After  : ", self.eid, self.name, self.sal)

madhu = Employee(100, 'Madhu Nettem', 20000, 5)
madhu.update_hike()
print("-------------------------------")
kiran = Employee(101,'Kiran G',10000, 3)
kiran.update_hike()
print("-------------------------------")
prakash = Employee(101,'Prakash S',10000, 1)
prakash.update_hike()
'''



class Employee:

    def __init__(self,eid,name,sal= 5000):
        self.eid = eid
        self.name = name
        self.sal = sal

    def update_hike(self, rating = 1):
        print("Emp details Before : ", self.eid, self.name, self.sal)
        if rating == 5:
            self.sal = self.sal + self.sal * 50 / 100
        elif rating == 3:
            self.sal = self.sal + self.sal * 15 / 100
        else:
            print(" No hike applicable for you.Improve yourself !!")

        print("Emp details After  : ", self.eid, self.name, self.sal)

madhu = Employee(100, 'Madhu Nettem', 20000)
madhu.update_hike(5)
print("-------------------------------")
kiran = Employee(101,'Kiran G',10000)
kiran.update_hike(3)
print("-------------------------------")
prakash = Employee(101,'Prakash S',10000)
prakash.update_hike(1)


class Employee(object):
    """This is employee class"""

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # Employee class has 3 behaviors
    def get_emp_hike(self, sal=1000):
        print("----In get employee hike----------")

    def get_emp_desn(self, hike):
        if (self.sal <= 100000):
            print(self.name, " is a softwatre trainee")
        else:
            print(self.name, " is a softwatre engineer")

    def xyz(self):
        pass


madhu = Employee(100, "MadhuNettem", 10000)  # CREATE
madhu.get_emp_desn(100)
madhu.get_emp_hike(100000)
madhu.xyz()