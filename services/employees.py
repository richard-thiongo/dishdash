from db import Database
import uuid
import functions

# Here we do the CRUD operations for the employees table e.g create, view, update, delete

class EmployeesService:
    # def __init__(self):
    #     self.db = Database()

    def createEmployee(self, first_name, last_name, employee_email, company_id, department_id, employee_status, profile_pic, employee_pasword):
        query = "insert into employees( employee_id, first_name, last_name, employee_email, company_id, department_id, employee_status, profile_pic, employee_password) values( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # employee_id = str(uuid.uuid4())
            # cursor = self.db.get_cursor()
            # data = (employee_id,first_name, last_name, employee_email, company_id,  department_id, employee_status, profile_pic, employee_pasword)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                employee_id = str(uuid.uuid4())
                data = (employee_id,first_name, last_name, employee_email, company_id,  department_id, employee_status, profile_pic, employee_pasword)
                cursor.execute(query, data)
                return True
        except Exception as e:
           # print(e)
            return False
        # finally:
        #     self.db.close() 

    # view employee using the company id 
    def viewEmployees(self, company_id):
        query = "SELECT * FROM employees WHERE company_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (company_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     employees = cursor.fetchall()
            #     print(employees)
            #     return employees
            with Database() as cursor:
                data = (company_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    employees = cursor.fetchall()
                    print(employees)
                    return employees
        except Exception as e:
            #print(e)
            return False
        # finally:
        #     self.db.close() 


    def viewEmployeeDepartment(self, department_id):
        query = "SELECT * FROM employees WHERE department_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (department_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     employees = cursor.fetchall()
            #     print(employees)
            #     return employees
            with Database() as cursor:
                data = (department_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    employees = cursor.fetchall()
                    print(employees)
                    return employees
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close() 


    def employeeeLogin(self, employee_email, password):
        query = "SELECT * FROM employees WHERE employee_email = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (employee_email)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     employee = cursor.fetchone()
            #     return employee
            with Database() as cursor:
                data = (employee_email)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    employee = cursor.fetchone()
                    return employee
        except Exception as e:
            # print(e)
            return False


    def employeeProfile(self, employee_email):
        query = "SELECT * FROM employees WHERE employee_email = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (employee_email)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     employee = cursor.fetchone()
            #     return employee  
            with Database() as cursor:
                data = (employee_email)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    employee = cursor.fetchone()
                    return employee
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()
        


    def updateEmployeeProfile(self, employee_id, first_name, last_name, employee_email, department_id, employee_status, profile_pic, employee_password):
        query = "UPDATE employees SET first_name = %s, last_name = %s, employee_email = %s, department_id = %s, employee_status = %s, profile_pic = %s, employee_password = %s WHERE employee_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (first_name, last_name, employee_email, department_id, employee_status, profile_pic, employee_password, employee_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (first_name, last_name, employee_email, department_id, employee_status, profile_pic, employee_password, employee_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close() 



    def deleteEmployee(self, employee_id):
        query = "DELETE FROM employees WHERE employee_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (employee_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (employee_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close() 




    







    







        





    