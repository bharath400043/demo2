'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(user = "postgres",
                            password = "1825",
                            host = "localhost", 
                            port = "5432")
    print("Conn type  :",type(conn))
    print("Connection :",conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Insert records to DEPT Table
    '''
    insert into DEPARTMENT (DEPTNO, DNAME, LOC) values(10, 'ACCOUNTING', 'NEW YORK')
    insert into DEPARTMENT values(20, 'RESEARCH', 'DALLAS')
    insert into DEPARTMENT values(30, 'SALES', 'CHICAGO')
    insert into DEPARTMENT values(40, 'OPERATIONS', 'BOSTON')
    '''
    query = ["insert into DEPARTMENT values(10, 'ACCOUNTING', 'NEW YORK')",
             "insert into DEPARTMENT values(20, 'RESEARCH', 'DALLAS')",
             "insert into DEPARTMENT values(30, 'SALES', 'CHICAGO')",
             "insert into DEPARTMENT values(40, 'OPERATIONS', 'BOSTON')"]
    for each in query:
        cursor.execute(each)
    print("----Records inserted into DEPT successfully-----")    
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()