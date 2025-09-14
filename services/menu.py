from db import Database
import uuid
import functions

# Here we do the CRUD operations for the menus table

class MenusService:
    def __init__(self):
        self.db = Database()


    # operations to create, view, update, delete, by the role of the restaurant
    # thr menu table has menu_price, menu_photo, menu_status, menu_description, menu_name, menu_id and restaurant_id

    def createMenu(self, menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id):

        query = "INSERT INTO menu (menu_id, menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            menu_id = str(uuid.uuid4())
            cursor = self.db.get_cursor()
            data = (menu_id, menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e) 
            return False
        finally:    
            self.db.close()



    def viewMenu(self, restaurant_id):

        query = "SELECT * FROM menu WHERE restaurant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (restaurant_id)
            cursor.execute(query, data)
            if cursor.rowcount  == 0:
                return False
            else:
                menu = cursor.fetchall()
                return menu  
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def updateMenu(self, menu_id, menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id):

        query = "UPDATE menu SET menu_name = %s, menu_description = %s, menu_price = %s, menu_photo = %s, menu_status = %s WHERE menu_id = %s and restaurant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (menu_name, menu_description, menu_price, menu_photo, menu_status, menu_id, restaurant_id )
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def deleteMenu(self, menu_id):

        query = "DELETE FROM menu WHERE menu_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (menu_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def viewMenuById(self, menu_id):

        query = "SELECT * FROM menu WHERE menu_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (menu_id)
            cursor.execute(query, data)
            if cursor.rowcount  == 0:
                return False
            else:
                menu = cursor.fetchone()
                return menu  
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


   



        


