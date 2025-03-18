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
    
    def show_data():
        pass 
    
       


new_employee=Employee(1,'elmahdy',44,'3-9-1980','01223146453','faculty of commerce','1-1-2020','elmahdy.tamam@gmail.com',False,10.0000)
#print(new_employee.id) 
my_sql=Mysql()
db_operation=DataHandler(my_sql)
'''
db_operation.configure_data("insert into employee(id,name,age,birth,phone,degree,hiredate,email,status_married,salary)values(%s,%s,%s,%s,%s,%s,%s,%s,%s);",args=(
 new_employee.id,new_employee.name,new_employee.age,new_employee.birthdate,new_employee.phone,new_employee.degree,new_employee.hiredate,
 new_employee.email,new_employee.status,new_employee.salary
))
'''
#db_operation.configure_data("insert into employee(id,name,age)values({id},{name},{age});")
db_operation.save_data(new_employee)



    
'''
 summary : Manager class is child class which inherits from the employee class 
   the manager also is a  employee

'''
class Manager(Employee):

    def __init__(self,id:int,name:str,age:str,birthdate:str,
                phone:str,degree:str,hiredate:str,email:str,status:bool,salary:float,departement_name:str,mgrid:int):
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
    def show_data():
        pass                  


new_manager=Manager(1,'elmahdy',44,'3-9-1980','01223146453','faculty of commerce','1-1-2020','elmahdy.tamam@gmail.com',False,10.0000,'hr',1)
print(new_manager.get_mgrid())





'''
summary: this class is a concrete class which has it's own implentation
'''
class Patient():
    def __init__(self,id,name,age,birthdate,phone,email,job):
        self.id=id
        self.name=name
        self.age=age
        self.birthdate=birthdate
        self.phone=phone
        self.email=email
        self.job=job
        
    def show_data():
        pass    

new_patient=Patient(100,'ahmed',20,'1-1-2000','01234563636','ahmed@yahoo.com','it')
print(new_patient.name)

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
    
    def show_data():
        pass         

my_doctor=Doctor(5000,'slaeh',35,'3-3-2017','012435678','faculty of medicine','2-2-2024','saleh@gmail.com',False,4.500,'surgical','executive',new_patient)
print(my_doctor.specialization)
print(my_doctor.patient.name)

'''
summary: DataEntry class is inherits from employee class 
         this class cannot access the Managers class
'''

class DataEntry(Employee):
    def __init__(self,patient:Patient):
        self.patient=patient
    
dataentry=DataEntry(new_patient)
print(dataentry.patient.email) 

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
    
    def print():
        pass
    
pres_details=Prescription_Details(1,my_doctor.name,new_patient.name,my_prescription_analyze,'18-03-2025')
print(pres_details.doctor)
print(pres_details.prescription.prescription_type)        
                        