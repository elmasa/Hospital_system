from abc import ABC, abstractmethod
from DAL import *

'''
    summary : Employee class is the parent class which is is an abstract class as we see many class
              participate in the same proprety 
              all classes can inherits from it but we can't create an object 
              if there is a method we must implement them 
'''
class Employee(ABC):
   

    def __init__(self,id:int,name:str,age:str,birthdate:str,
    phone:str,degree:str,hiredate:str,email:str,status:bool,salary:float):
        if name=='' or email=='':
            raise ValueError( 'value cannot be empty')
        if("@" not in email):
            raise ValueError('email not in correct format')
        if not(isinstance(age,int)) or not isinstance(salary,float):
            raise TypeError('invalid data type')
        self.id=id
        self.name=name
        self.age=age
        self.birthdate=birthdate
        self.phone=phone
        self.degree=degree
        self.hiredate=hiredate
        self.email=email
        self.status=status
        self.salary=salary 
   
    def show_data(self):
        print(f"successfully created new employee with the following info: employee id is {self.id} \n employee name is {self.name} ") 
    
       


new_employee=Employee(5,'elmahdy',44,'3-9-1980','01223146453','faculty of commerce','1-1-2020','elmahdy.tamam@gmail.com',False,100.00)
Employee.show_data(new_employee)

emp_sql=Mysql()
db_operation=DataHandler(emp_sql)
emp_data=(new_employee.id,new_employee.name,new_employee.age,new_employee.birthdate,new_employee.phone,new_employee.degree,new_employee.hiredate,
 new_employee.email,new_employee.status,new_employee.salary)

emp_cursor=Mysql.connection.cursor()
emp_cursor.execute("insert into employee(id,name,age,birth,phone,degree,hiredate,email,status_married,salary)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",emp_data)

emp_sql.connection.commit()
emp_sql.connection.close()


    
'''
 summary : Manager class is child class which inherits from the employee class 
   the manager also is a  employee

'''
class Manager(Employee):

    def __init__(self,id:int,name:str,age:str,birthdate:str,
                phone:str,degree:str,hiredate:str,email:str,status:bool,salary:float,departement_name:str,mgrid:int):
        if name=='' or email=='' or departement_name=='':
            raise ValueError( 'value cannot be empty')
        if("@" not in email):
            raise ValueError('email not in correct format')
        if not(isinstance(age,int)) or not isinstance(salary,float):
            raise TypeError('invalid data type')
        self.id=id
        self.name=name
        self.age=age
        self.birthdate=birthdate
        self.phone=phone
        self.degree=degree
        self.hiredate=hiredate
        self.email=email
        self.status=status
        self.salary=salary 
        self.departement_name=departement_name
        self.__mgrid=mgrid
        
        '''
        dataentry=DataEntry()
        
        if isinstance(dataentry,DataEntry):
            raise TypeError('invalid data entry cannot access the Manager class')
        else:   
          self.__mgrid=mgrid
        ''' 
        

    '''
    summary: this method is used to get the manager id as 
         it's private field which is encapsulated 
    ''' 
    def get_mgrid(self):
        return self.__mgrid
          
    def set_mgrid(self,new_mgrid:int):
        self.__mgrid=new_mgrid 
         
    def show_data(self):
        print(f"successfully created new manager with the following info: manager id is {self.id} \n manger name is {self.name} ")     


new_manager=Manager(1,'elmahdy',44,'3-9-1980','01223146453','faculty of commerce','1-1-2020','elmahdy.tamam@gmail.com',False,10000.0,'hr',1)
Manager.show_data(new_manager)
'''
manager_sql=Mysql()
db_operation=DataHandler(manager_sql)
data=(new_manager.id,new_manager.name,new_manager.age,new_manager.birthdate,new_manager.phone,new_manager.degree,
      new_manager.hiredate,new_manager.email,new_manager.status,new_manager.salary,new_manager.departement_name,
      new_manager.get_mgrid())
mananger_cursor=Mysql.connection.cursor()
mananger_cursor.execute("insert into manager(id,name,age,birthdate,phone,degree,hiredate,email,status_married,salary,department_name,mgr_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",data)

manager_sql.connection.commit()
manager_sql.connection.close()
'''

'''
summary: this class is a concrete class which has it's own implentation
'''
class Patient():
    def __init__(self,id,name,age,birthdate,phone,email,job):
        if name=='' or email=='' or phone=='':
            raise ValueError( 'value cannot be empty')
        if("@" not in email):
            raise ValueError('email not in correct format')
        if not(isinstance(age,int)):
            raise TypeError('invalid data type')
        self.id=id
        self.name=name
        self.age=age
        self.birthdate=birthdate
        self.phone=phone
        self.email=email
        self.job=job
        
    def show_data(self):
         print(f"successfully created new patient with the following info: patient id is {self.id} \n patient name is {self.name} ")   

new_patient=Patient(100,'ahmed',20,'1-1-2000','01234563636','ahmed@yahoo.com','it') 


'''
summary: this class inherits from employee class
'''
class Doctor(Employee):
    '''
    summary: this class constructor we must create a patient 
    as this relation is composition as the doctor have a patient 
    '''
    def __init__(self,id:int,name:str,age:str,birthdate:str,
            phone:str,degree:str,hiredate:str,email:str,status:bool,salary:float,specialiazation:str,title:str,patient:Patient):
        if name=='' or email=='' or specialiazation=='':
            raise ValueError( 'value cannot be empty')
        if("@" not in email):
            raise ValueError('email not in correct format')
        if not(isinstance(age,int)):
            raise TypeError('invalid data type')
       
        self.id=id
        self.name=name
        self.age=age
        self.birthdate=birthdate
        self.phone=phone
        self.degree=degree
        self.hiredate=hiredate
        self.email=email
        self.status=status
        self.salary=salary 
        self.specialization=specialiazation
        self.title=title
        self.patient=patient  
    
    def show_data(self):
        print(f"successfully created new doctor with the following info: doctor id is {self.id} \n doctor name is {self.name} \n specialized in {self.specialization} ")        

my_doctor=Doctor(5000,'slaeh',35,'3-3-2017','012435678','faculty of medicine','2-2-2024','saleh@gmail.com',False,4.500,'surgical','executive',new_patient.id)
Doctor.show_data(my_doctor)
'''
doctor_sql=Mysql()
db_operation=DataHandler(doctor_sql)
doctor_data=(my_doctor.id,my_doctor.name,my_doctor.age,my_doctor.birthdate,my_doctor.phone,
      my_doctor.degree,my_doctor.hiredate,my_doctor.email,my_doctor.status,my_doctor.salary,
      my_doctor.specialization,my_doctor.title,new_patient.id)
#print(data)
doctor_cursor=Mysql.connection.cursor()
doctor_cursor.execute("insert into Doctor(id,name,age,birthdate,phone,degree,hiredate,email,status_married,salary,specialization,title,patient_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",doctor_data)
doctor_sql.connection.commit()
doctor_sql.connection.close()
'''

'''
summary: DataEntry class is inherits from employee class 
         this class cannot access the Managers class
'''

class DataEntry(Employee):
    def __init__(self,patient:Patient):
        self.patient=patient
    
    def show_data(self):
        print(f"successfully created new patient with the following info: patient id is {self.id} \n patient name is {self.name} ")  

   
dataentry=DataEntry(new_patient)
DataEntry.show_data(new_patient)
'''
dataentry_sql=Mysql()
db_operation=DataHandler(dataentry_sql)
dataentry_data=(new_patient.id,new_patient.name,new_patient.age,new_patient.birthdate,new_patient.phone,new_patient.email,new_patient.job)
dataentry_cursor=Mysql.connection.cursor()
dataentry_cursor.execute("insert into patient(id,name,age,birthdate,phone,email,job)values(%s,%s,%s,%s,%s,%s,%s);",dataentry_data)

dataentry_sql.connection.commit()
dataentry_sql.connection.close()
'''

'''
summary: this class is an abstract class and the method is decorated as abstract 
         there is no implementation any class inherits from it must implement the abstract method
'''
class Prescription_Type(ABC):
    @abstractmethod
    def get_prescription():
        pass

class Prescription_Medicine(Prescription_Type):
    
    def get_prescription(self): 
        return "Medicine Prescription"

class Prescription_Analyze(Prescription_Type):
      
      def get_prescription(self): 
        return "Analyze Prescription"

class Prescription_Scan(Prescription_Type):
      
      def get_prescription(self): 
        return "Scan Prescription"

class Prescription_SurgicalOperation(Prescription_Type):
      
      def get_prescription(self): 
        return "Surgical_Operation Prescription" 

'''
summary: this class is the factory class for creating the prescription 
'''
class PrescriptionFactory:
    '''
    summary : this method is a static which we use without take an instance of the class
    '''
    @staticmethod
    def create_prescription(perscription_type:Prescription_Type):
        presc_type = perscription_type.get_prescription()
        return Prescription(presc_type)

'''
summary : this class is to get the prescription type 
'''
class Prescription():
    
    
    def __init__(self,prescription_type:Prescription_Type):
          self.prescription_type=prescription_type
       
    
    def __print__(self):
      print(self.prescription_type)
            
           
my_prescription_analyze=PrescriptionFactory.create_prescription(Prescription_Analyze()) 
print(my_prescription_analyze.__print__())           


'''
summary: this class inherits from prescription class
         this class is responsible for the prescription details
         the prescription details is compose of the doctor and patient and the prescription type
'''
class Prescription_Details(Prescription):
    '''
    summary: we must create the doctor,patient,prescription 
    '''
    def __init__(self,id:int,doctor:Doctor,patient:Patient,prescription:Prescription,prescription_date:str):
        self.id=id
        self.doctor=doctor
        self.patient=patient
        self.prescription=prescription
        self.prescription_date=prescription_date
    
    def show_data(self):
        print(f"successfully created prescription with the following info: prescription id is {self.id} \n doctor name is {my_doctor.name} \n specialized in {my_doctor.specialization}  wrote {self.prescription.prescription_type} for patient name {new_patient.name} on {self.prescription_date} ") 
pres_details=Prescription_Details(1,my_doctor.id,new_patient.id,my_prescription_analyze,'18-03-2025')
Prescription_Details.show_data(pres_details)
'''
pres_sql=Mysql()
db_operation=DataHandler(pres_sql)
pres_data=(pres_details.id,my_doctor.id,new_patient.id,my_prescription_analyze.prescription_type,pres_details.prescription_date)
pres_cursor=Mysql.connection.cursor()
pres_cursor.execute("insert into Prescription_details(id,doctor_id,patient_id,prescription,prescription_date)values(%s,%s,%s,%s,%s);",data)
pres_sql.connection.commit()
pres_sql.connection.close()
'''
        
                        