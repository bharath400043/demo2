class Employee:

    def __init__(self, eid, name, sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

# Constructor Overloading
madhu = Employee(101,'Madhu Nettem')
kiran = Employee(102,'Kiran Kumar',20000)
