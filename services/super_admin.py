from db import Database
import functions

class SuperAdminService:
    # def __init__(self):
    #     self.db = Database()


    def createSuperAdmin(self, username, password):
        query = "INSERT INTO super_admin (username, password) VALUES (%s, %s)"
        try:
            # cursor = self.db.get_cursor()
            # data = (username, password)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (username, password)
                cursor.execute(query, data)
                self.db.commit()
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close() 




    def superAdminLogin(self, username, password):
        query = "SELECT * FROM super_admin WHERE username = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (username)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     result = cursor.fetchone()
            #     if  functions.has_verify(password, result['password']):
            #         return result 
            #     else:
            #         return False
            with Database() as cursor:
                data = (username)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    result = cursor.fetchone()
                    if  functions.has_verify(password, result['password']):
                        return result 
                    else:
                        return False
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()




