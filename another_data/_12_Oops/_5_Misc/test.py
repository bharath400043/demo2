

from _12_Oops._3_sal_hike_emp import Employee



madhu = Employee(1000,'MAdhuN',20000) # Permission
#madhu.update_hike()


if __name__ == '__main__':
    print("Hike details ")
    madhu.update_hike()
    print(madhu.eid,madhu.name,madhu.sal)