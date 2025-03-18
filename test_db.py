import pytest 
import pymysql
from DAL import *

@pytest.fixture
def return_connection() :
    connection = pymysql.connect(
    host = 'localhost',user = 'root', 
    password='1234',database='hospital')
    return connection
        

def test_connection(return_connection) :
    
    connection = return_connection
    assert connection is not None
    print( 'connection success !' )

    
    
def test_first_query(return_connection) :
    connection = return_connection
    my_cursor = connection.cursor()
    my_cursor.execute('SELECT 1;')
    row = my_cursor.fetchone()
    assert row == (1,)
    print( 'First query Success !' ) 
    connection.close()
    
def test_create_db(return_connection) :
    
    connection = return_connection
    my_cursor = connection.cursor()
    my_cursor.execute('CREATE DATABASE IF NOT EXISTS test_hospital;')
    my_cursor.execute('SHOW DATABASES;')
    databases = my_cursor.fetchall()
    assert ('test_hospital',) in databases
    print( 'Creation of the database success !' )
    my_cursor.execute('DROP DATABASE IF EXISTS test;') 
    connection.close    

def test_get_employee(return_connection):
    Connection=return_connection
    my_data=Connection.cursor()
    my_data.execute('select * from employee where id=%s;',1)
    row=my_data.fetchone()
    assert row==(1,'elmahdy',44,'3-9-1980','01223146453','faculty of commerce','1-1-2020','elmahdy.tamam@gmail.com',False,10.0000) 
    print ('get data success')
    Connection.close()

def test_savedata():
    my_sql=Mysql()
    db_operation=DataHandler(my_sql)
    db_operation.save_data(' (id = 1 ,name = "ahmed", age = 25) ')  
    assert  'Succesfully Connecting to MYSQL Database '
    assert  ' Saving  (id = 1 ,name = "ahmed", age = 25)  to MYSQL Database '  
    
def test_deletedata():
    my_sql=Mysql()
    db_operation=DataHandler(my_sql) 
    db_operation.delete_data('(id=1) ')
    assert 'Delete  ( id=1) from MYSQL Database' 
    
def test_searchdata():
    my_sql=Mysql()
    db_operation=DataHandler(my_sql) 
    db_operation.search_data('(id=1) ') 
    assert 'found  (id =1)  from MYSQL Database'    
    