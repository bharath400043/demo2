'''
Created on Mar 20, 2020

@author: madhu
'''
from _21_1_DB_Access._03_EMP_Refactored.utilities import conn
#Step1 : Get connection
def process_text_data(file_name):
    emp_records = []
    with open(file_name) as e_data:
        data = e_data.read().split('\n')
        for each in data:
            emp_records.append(each.split(', '))
    #print(emp_records)
    for each in emp_records:
        print(each)
        empno = int(each[0])
        ename = each[1]
        job = each[2]
        if each[3] == 'null':
            mgr = None
        else:
            mgr = each[3]
        hiredate = None
        sal = int(each[5])
        if each[6] =='null':
            comm = None
        else:
            comm = int(each[6])
        deptno = int(each[7])
        li = []
        li.extend([empno,ename,job,mgr,hiredate,sal,comm,deptno])
        return li

try:
    cursor = conn.cursor()
    f_name = 'emp_data.txt'
    #Step3 : Retrieve emp data
    li_data = process_text_data(f_name)
    query = 'INSERT INTO EMP VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query,tuple(li_data))
    print("----Records inserted into DEPT successfully-----")
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()