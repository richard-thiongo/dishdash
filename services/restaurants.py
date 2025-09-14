from db import Database
import uuid
import functions

class RestaurantsService:
    def __init__(self):
        self.db = Database()



    def createRestaurant(self, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password):
        query = "INSERT INTO restaurants (restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            restaurant_id = str(uuid.uuid4())
            cursor = self.db.get_cursor()
            data = (restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e) 
            return False
        finally:    
            self.db.close()




    def restaurantLogin(self, restaurant_email, restaurant_password):
        query = "SELECT * FROM restaurants WHERE restaurant_email = %s"
        try:
            cursor = self.db.get_cursor()
            data = (restaurant_email)
            cursor.execute(query, data)
            if cursor.rowcount  == 0:
                return False
            else:
                result = cursor.fetchone()
                if  functions.has_verify(restaurant_password, result['restaurant_password']):
                    return result 
                else:
                    return False
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def restaurantProfile(self, restaurant_id):
        query = "SELECT * FROM restaurants WHERE restaurant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (restaurant_id)
            cursor.execute(query, data)
            if cursor.rowcount  == 0:
                return False
            else:
                restaurant = cursor.fetchone()
                return restaurant  
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()



    def updateRestaurant(self, restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password):
        query = "UPDATE restaurants SET restaurant_name = %s, restaurant_address = %s, restaurant_email = %s, till_no = %s, restaurant_description = %s, restaurant_status = %s, restaurant_password = %s WHERE restaurant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password, restaurant_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()




    def deleteRestaurant(self, restaurant_id):
        query = "DELETE FROM restaurants WHERE restaurant_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (restaurant_id)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    def viewRestaurants(self):
        query = "SELECT * FROM restaurants"
        try:
            cursor = self.db.get_cursor()
            cursor.execute(query)
            if cursor.rowcount  == 0:
                return False
            else:
                restaurants = cursor.fetchall()
                return restaurants
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()


    




    