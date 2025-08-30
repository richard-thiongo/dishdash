from db import Database
import uuid

# Here we do the CRUD operations for the companies table

class CompanyService:
    def __init__(self):
        self.db = Database()

    def createCompany(self, company_name, company_address, company_email, company_phone, company_logo, password):
        query = "INSERT INTO companies (company_id, company_name, company_address, company_email, company_phone, company_logo, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            company_id = str(uuid.uuid4())
            cursor = self.db.get_cursor()
            data = (company_id, company_name, company_address, company_email, company_phone, company_logo, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e) 
            return False
        finally:
            self.db.close()                                                                                                                    

