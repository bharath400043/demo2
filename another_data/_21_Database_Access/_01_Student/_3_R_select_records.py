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
    #Step3 : Execute sql query 
    cursor.execute("SELECT * FROM STUDENT")
    #print("Selection : ",cursor.fetchall())
    #Step4 : Retrieve Records
    print("\n-----Retrieving records from db table Test-------")
    records = cursor.fetchall()
    print(records)
    for each in records:
        print(each)
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()