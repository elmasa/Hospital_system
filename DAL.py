from abc import ABC , abstractmethod
import pymysql


'''
summary: this class is an abstract class we can inhertis from it 
         we must implement our methdods as all method are abstract 
'''

class Database(ABC):
    '''
    summary: this method is used to connect to database
    '''
    @abstractmethod
    def connect_db(self):
        pass
    
    '''
    summary: this method is used to insert data in a database
    '''
    @abstractmethod
    def insert_db(self,data):
        pass

    '''
    summary: this method is used to delete data from database
    '''    
    @abstractmethod
    def delete_db(self,data):
        pass

    '''
    summary: this method is used to search for data in the database
    '''    
    @abstractmethod
    def search_db(self,data):
        pass

'''
summary: this class is used as the operation for the mysql database 
        check the connection , CRUD operations
'''
class Mysql(Database):
    
    connection=pymysql.connect(host='localhost',user='root',
    password='1234',database='hospital')
    my_cursor=connection.cursor()

    def connect_db(self):
        #implementation for connect to mysql database
   
    
     if  Mysql.connection.connect:
       print( 'Succesfully Connecting to MYSQL Database ' )
     else:
        raise ConnectionError('failed to connect to MYSQL database')   
    
    def insert_db(self,data):
       
        #row=my_cursor.execute(data)
        print( f'Saving {data} to MYSQL Database ' )

    def delete_db(self,data):
        print( f'Delete {data} from MYSQL Database ' )   

    def search_db(self,data):
         print( f'found {data} from MYSQL Database ' )
    


class DataHandler :
    def __init__(self, database : Database) :
        if (isinstance(database,Database)):
           self.database = database
           self.database.connect_db()
        else:
            raise TypeError('invalid database  type')
        
    def configure_data(self,data):
        Mysql.connection.connect()
        my_cursor=my_sql.connection.cursor()
        row= my_cursor.execute(data)
        
        Mysql.connection.commit()
        Mysql.connection.close()   
        
    def save_data(self, data) :
        
        self.database.insert_db(data)
        
    def delete_data(self,data) :
         self.database.delete_db(data) 
         
    def search_data(self,data):
        self.database.search_db(data)      
            
 
my_sql=Mysql()
db_operation=DataHandler(my_sql)
db_operation.configure_data("insert into employee(id,name,age,birth,phone,degree,hiredate,email,status_married,salary)values(2,'ahmed',24,'3-9-2000','0123456666','faculty of commerce','1-1-2020','ahmed@gmail.com',False,5000);")

db_operation.save_data(' (id = 1 ,name = "ahmed", age = 25) ') 
db_operation.search_data(' (id =1) ')
db_operation.delete_data( ' ( id=1)')

        