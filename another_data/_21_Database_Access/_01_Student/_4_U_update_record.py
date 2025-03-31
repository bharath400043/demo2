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
    cursor = conn.cursor()
    res = cursor.execute("UPDATE STUDENT set name = 'MadhuSudhanNaidu Nettem' where sid = 103")
    print("Record Updated successfully : ",res)
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()