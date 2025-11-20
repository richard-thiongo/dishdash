from db import Database
import uuid
import functions

# Here we do the CRUD operations for the companies table

class CompanyService:
    # def __init__(self):
    #     self.db = Database()

    def createCompany(self, company_name, company_address, company_email, company_phone, company_logo, password):
        query = "INSERT INTO companies (company_id, company_name, company_address, company_email, company_phone, company_logo, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            #  Using context manager
            with Database() as cursor:
                company_id = str(uuid.uuid4())
                data = (company_id, company_name, company_address, company_email, company_phone, company_logo, password)
                cursor.execute(query, data)
                return True
            # company_id = str(uuid.uuid4())
            # cursor = self.db.get_cursor()
            # data = (company_id, company_name, company_address, company_email, company_phone, company_logo, password)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            
        except Exception as e:
            # print(e) 
            return False
        # finally:    
        #     self.db.close()


    def companyLogin(self, company_email, password):
        query = "SELECT * FROM companies WHERE company_email = %s"
        try:
            with Database() as cursor:
                data = (company_email,) 
                cursor.execute(query, data)

                if cursor.rowcount == 0:
                    print(f"Login failed: company '{company_email}' not found.")
                    return None  

                result = cursor.fetchone()  # fetch inside the context

                # Verify password
                if functions.hash_verify(password, result['password']):
                    return result
                else:
                    print(f"Login failed: wrong password for '{company_email}'.")
                    return None
        except Exception as e:
            print("Login error:", e)
            return None


    # make a function to get company profile by company_id
    def companyProfile(self, company_id):
        query = "SELECT * FROM companies WHERE company_id = %s"
        try:
            with Database() as cursor:
                data = (company_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    company = cursor.fetchone()
                    return company
            # cursor = self.db.get_cursor()
            # data = (company_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     company = cursor.fetchone()
            #     return company  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()

    # make a function for the company to  create a department

    
    def createDepartment(self, department_name, company_id):
        # Validate company_id exists
        check_query = "SELECT * FROM companies WHERE company_id = %s"
        try:
            with Database() as cursor:
                data = (company_id)
                cursor.execute(check_query, data)
                if cursor.fetchone() is None:
                    return False

            # Proceed with creating department
                department_id = str(uuid.uuid4())
                insert_query = "INSERT INTO departments (department_id, department_name, company_id) VALUES (%s, %s, %s)"
                data = (department_id, department_name, company_id)
                cursor.execute(insert_query, data)
                print(cursor.rowcount)
                return True
                

            # Using context manager
            # cursor = self.db.get_cursor()
            # cursor.execute(check_query, (company_id))
            # if cursor.fetchone() is None:
            #     return False

            # # Proceed with creating department
            # department_id = str(uuid.uuid4())
            # insert_query = "INSERT INTO departments (department_id, department_name, company_id) VALUES (%s, %s, %s)"
            # cursor.execute(insert_query, (department_id, department_name, company_id))
            # print(cursor.rowcount)
            # self.db.commit()
            # return True
        except Exception as e:
            #print(e)
            return False
        # finally:
        #     self.db.close()

    # make a function for company to get all departments
    def getDepartments(self, company_id):
        query = "SELECT * FROM departments WHERE company_id = %s"
        try:
            with Database() as cursor:
                data = (company_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    departments = cursor.fetchall()
                    return departments
            # cursor = self.db.get_cursor()
            # data = (company_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     departments = cursor.fetchall()
            #     return departments  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()



    # make a function to update department
    def updateDepartment(self, department_id, department_name):
        query = "UPDATE departments SET department_name = %s WHERE department_id = %s"
        try:
            with Database() as cursor:
                data = (department_name, department_id)
                cursor.execute(query, data)
                self.db.commit()
                return True
            # cursor = self.db.get_cursor()
            # data = (department_name, department_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close() 



    #  make a function to delete department
    def deleteDepartment(self, department_id):
        query = "DELETE FROM departments WHERE department_id = %s"
        try:
            with Database() as cursor:
                data = (department_id)
                cursor.execute(query, data)
                self.db.commit()
                return True
            # cursor = self.db.get_cursor()
            # data = (department_id)
            # cursor.execute(query, data)
            # self.db.commit   
            # return True
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close() 


    # make a function to get department by id
    def getDepartmentById(self, department_id):
        query = "SELECT * FROM departments WHERE department_id = %s"
        try:
            with Database() as cursor:
                data = (department_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    department = cursor.fetchone()
                    return department
            # cursor = self.db.get_cursor()
            # data = (department_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     department = cursor.fetchone()
            #     return department  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()



    # make a function to count all departments
    def countDepartments(self, company_id):
        query = "SELECT COUNT(*)as count FROM departments WHERE company_id = %s"
        try:
            with Database() as cursor:
                data = (company_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    count = cursor.fetchone()
                    return count
            # cursor = self.db.get_cursor()
            # data = (company_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     count = cursor.fetchone()
            #     return count  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()


    # make a function to get all employees by department_id
    def getEmployeesByDepartment(self, department_id):
        query = "SELECT * FROM employees WHERE department_id = %s"
        try:
            with Database() as cursor:
                data = (department_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    employees = cursor.fetchall()
                    return employees
            # cursor = self.db.get_cursor()
            # data = (department_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     employees = cursor.fetchall()
            #     return employees  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()




    # Make a function to count the number of employees by department
    def countEmployeesByDepartment(self, department_id):
        query = "SELECT COUNT(*)as count3    FROM employees WHERE department_id = %s"
        try:
            with Database() as cursor:
                data = (department_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    count = cursor.fetchone()
                    return count
            # cursor = self.db.get_cursor()
            # data = (department_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     count = cursor.fetchone()
            #     return count  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()
    


    # make a function to count all employees
    def countAllEmployees(self, company_id):
        query = "SELECT COUNT(*)as count2 FROM employees WHERE company_id = %s"
        try:
            with Database() as cursor:
                data = (company_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    count = cursor.fetchone()
                    return count
            # cursor = self.db.get_cursor()
            # data = (company_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     count = cursor.fetchone()
            #     return count  
        except Exception as e:
            # print(e)
            return False
        # finally:
        #     self.db.close()
        

    




    

       
       

                                                                                                                    