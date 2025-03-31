'''
Created on Mar 20, 2020

@author: madhu

UI --> Python --> Database

'''
import psycopg2
try:
    conn = psycopg2.connect(user = "postgres",
                            password = "1825",
                            host = "localhost",
                            port = "5432")
    cursor = conn.cursor()
    stud_id = int(input("Enter student id : "))
    cursor.execute("DELETE FROM STUDENT WHERE SID = {0}".format(stud_id))
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()