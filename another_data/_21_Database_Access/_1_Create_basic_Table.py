'''
#Step1 : Get connection
#Step2 : Get cursor on db connection
#Step3 : Prepare SQL Query
#Step4 : Execute SQL query
#Step5 : Commit the transaction
'''

# Step1 : Get connection
import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user = "postgres",
                            password = "vn2",
                            host = "localhost",
                            port = "5432")
    print("Connection type :",type(conn))  # connection
    # Step2 : Get cursor on db connection
    cur = conn.cursor()  # cursor
    print("Cursor  type :",type(cur))
    # Step3 : Prepare SQL Query
    #query = "create table DEPT(deptno INT,dname TEXT,loc text,primary key(deptno))"
    query = "insert into DEPT values(40, 'SOFTWARE', 'BANGALORE')"
    #Step4 : Execute SQL query
    cur.execute(query)
    # Step5 : Commit the transaction
    conn.commit()
    print("Table created successfully")
except Exception as ex:
    print("Exception occured during db transaction : ",ex)
finally:
    cur.close()
    conn.close()

'''
try:
    conn = psycopg2.connect(database="postgres",
                            user = "postgres",
                            password = "vn2",
                            host = "localhost",
                            port = "5432")
    cur = conn.cursor()
    query = "CREATE TABLE cust_data2(name VARCHAR(255), address VARCHAR(255))"
    cur.execute(query)
    conn.commit()
except Exception as ex:
    print("Exception occured during db transaction : ",ex)
finally:
    cur.close()
    conn.close()
'''