'''
Created on Mar 20, 2020

@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/
'''
from _21_1_DB_Access._03_EMP_Refactored.utilities import conn, emp_create_q

try:
    # Step2: get cursor object
    cursor = conn.cursor()
    #Step3 : Execute sql query
    cursor.execute(emp_create_q)
    print("EMP Table Created")
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()
