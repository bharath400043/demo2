'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection

def get_data_from_txt():
    emp_records = []
    with open('edata.txt') as e_data:
        data = e_data.read().split('\n')
    for each in data:
        emp_records.append(each.split(', '))
    #print(emp_records)
    li = []
    for each in emp_records:
         #print([empno,ename,job,mgr,hiredate,sal,comm,deptno])
        li.append([each[0],each[1],each[2],each[3],each[4],each[5]])
    return li
try:
    conn = psycopg2.connect(database="postgres", 
                            user = "postgres", 
                            password = "vn2", 
                            host = "localhost", 
                            port = "5432")
    print("Conn type  :",type(conn))
    print("Connection :",conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Retrieve emp data
    data = get_data_from_txt()
    query = 'INSERT INTO Employee VALUES(%s,%s,%s,%s,%s,%s)'
    print(data)
    for each in data:
        print(each)
        cursor.execute(query,tuple(each))
    #Step4: Commit the transaction
    conn.commit()
    print("----Records inserted into EMPLOYEE successfully-----")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()