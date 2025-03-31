'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2

try:
    conn = psycopg2.connect(user = "postgres",
                            password = "1825",
                            host = "localhost", 
                            port = "5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Execute sql query 
    res = cursor.execute("INSERT INTO STUDENT VALUES(103, 'MADHU', 'ABC')")
    cursor.execute("INSERT INTO STUDENT VALUES(104, 'Prakash', 'AREM')")
    cursor.execute("INSERT INTO STUDENT VALUES(105, 'Kiran', 'VN2')")
    print("Insertion : ",res)
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()