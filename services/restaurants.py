from db import Database
import uuid
import functions

class RestaurantsService:
    # def __init__(self):
    #     self.db = Database()



    def createRestaurant(self, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password):
        query = "INSERT INTO restaurants (restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            # restaurant_id = str(uuid.uuid4())
            # cursor = self.db.get_cursor()
            # data = (restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                restaurant_id = str(uuid.uuid4())
                data = (restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e) 
            return False
        # finally:    
        #     self.db.close()




    def restaurantLogin(self, restaurant_email, restaurant_password):
        query = "SELECT * FROM restaurants WHERE restaurant_email = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (restaurant_email)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     result = cursor.fetchone()
            #     if  functions.has_verify(restaurant_password, result['restaurant_password']):
            #         return result 
            #     else:
            #         return False
            with Database() as cursor:
                data = (restaurant_email)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    result = cursor.fetchone()
                    if  functions.hash_verify(restaurant_password, result['restaurant_password']):
                        return result 
                    else:
                        return False
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()




    def restaurantProfile(self, restaurant_id):
        query = "SELECT * FROM restaurants WHERE restaurant_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (restaurant_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     restaurant = cursor.fetchone()
            #     return restaurant  
            with Database() as cursor:
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
        # finally:
        #     self.db.close()



    def updateRestaurant(self, restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password):
        query = "UPDATE restaurants SET restaurant_name = %s, restaurant_address = %s, restaurant_email = %s, till_no = %s, restaurant_description = %s, restaurant_status = %s, restaurant_password = %s WHERE restaurant_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password, restaurant_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, restaurant_password, restaurant_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()




    def deleteRestaurant(self, restaurant_id):
        query = "DELETE FROM restaurants WHERE restaurant_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (restaurant_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (restaurant_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()


    def viewRestaurants(self):
        query = "SELECT * FROM restaurants"
        try:
            # cursor = self.db.get_cursor()
            # cursor.execute(query)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     restaurants = cursor.fetchall()
            #     return restaurants
            with Database() as cursor:
                cursor.execute(query)
                if cursor.rowcount  == 0:
                    return False
                else:
                    restaurants = cursor.fetchall()
                    return restaurants
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()



    def totalOrders(self, restaurant_id):
        query = """
        SELECT COUNT(o.order_id) AS total_orders
        FROM orders o
        JOIN menu m ON o.menu_id = m.menu_id
        WHERE m.restaurant_id = %s
        """
        try:
            with Database() as cursor:
                data = (restaurant_id,)
                cursor.execute(query, data)
                if cursor.rowcount == 0:
                    return 0
                else:
                    result = cursor.fetchone()
                    return result['total_orders'] if result and 'total_orders' in result else 0
        except Exception as e:
            print(e)
            return 0



    def viewOrdersByRestaurant(self, restaurant_id):
        query = """
            SELECT 
                o.order_id,
                c.company_name,
                m.menu_name,
                m.menu_photo,
                m.menu_price,
                o.order_date,
                o.is_paid
            FROM orders o
            JOIN employees e ON o.employee_id = e.employee_id
            JOIN companies c ON e.company_id = c.company_id
            JOIN menu m ON o.menu_id = m.menu_id
            WHERE m.restaurant_id = %s
            ORDER BY o.order_date DESC
            """
        try:
            with Database() as cursor:
                cursor.execute(query, (restaurant_id,))
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            return []






    




    