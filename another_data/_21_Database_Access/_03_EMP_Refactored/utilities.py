'''
Created on Mar 20, 2020

@author: madhu

helper properties classes constants
'''
import psycopg2
conn = psycopg2.connect(database="postgres", 
                        user = "postgres", 
                        password = "vn2", 
                        host = "localhost", 
                        port = "5432")

emp_create_q = """
        create table EMP_40(empno INT, 
                            ename TEXT, 
                            job TEXT,
                            mgr INT,
                            hiredate DATE,
                            sal INT,
                            comm INT,
                            deptno INT,
                            primary key(empno),  
                            foreign key(deptno) references dept(deptno))
        """

emp_insert_q = 'INSERT INTO EMP_40 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
emp_update_sal = "UPDATE EMP_40 set sal = 25000 where empno = 7839"
emp_data_sel = "SELECT * FROM EMP_40"