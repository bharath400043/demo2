'''
Created on Mar 20, 2020

@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/

UI    --->   Python   --->  Database

'''
#Step1 : Get connection
#Step2 : Get cursor on db connection
#Step3: Prepare SQL Query
#Step3 : Execute sql query
#Step4: Commit the transaction

import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                            user = "postgres", 
                            password = "1825",
                           )
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    print(type(cursor))
    #Step3: Prepare SQL Query
    query = "CREATE TABLE STUDENT(SID INTEGER PRIMARY KEY, NAME VARCHAR(255),SCHOOL VARCHAR(255))"
    #Step3 : Execute sql query 
    cursor.execute(query)
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()
