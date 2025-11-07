from db import Database
import uuid
import functions

# Here we do the CRUD operations for the companies table

class OrdersService:
    # def __init__(self):
    #     self.db = Database()    



    # the table for orders has the columns payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price  

# 1
    def createOrder(self, payment_id, order_date, is_paid, menu_id, employee_id,  menu_price):

        query = "INSERT INTO orders (payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            # order_id = str(uuid.uuid4())
            # cursor = self.db.get_cursor()
            # data = (payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                order_id = str(uuid.uuid4())
                data = (payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()

# 2
    # view orders by restaurant id
    def viewOrders(self, restaurant_id):

        query = "SELECT * FROM orders WHERE restaurant_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (restaurant_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (restaurant_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()



# 3
    def updateOrder(self, order_id, payment_id, order_date, is_paid, menu_id, employee_id,  menu_price):

        query = "UPDATE orders SET payment_id = %s, order_date = %s, is_paid = %s, menu_id = %s, employee_id = %s, order_id = %s, menu_price = %s WHERE order_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price, order_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (payment_id, order_date, is_paid, menu_id, employee_id, order_id, menu_price, order_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()



# 4
    def deleteOrder(self, order_id):

        query = "DELETE FROM orders WHERE order_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (order_id)
            # cursor.execute(query, data)
            # self.db.commit()
            # return True
            with Database() as cursor:
                data = (order_id)
                cursor.execute(query, data)
                return True
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()


# 5
    def viewOrderById(self, order_id):

        query = "SELECT * FROM orders WHERE order_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (order_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     order = cursor.fetchone()
            #     return order
            with Database() as cursor:
                data = (order_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    order = cursor.fetchone()
                    return order
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()



# 6
    def viewOrdersByEmployee(self, employee_id):
        query = "SELECT * FROM orders WHERE employee_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (employee_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (employee_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()



# 7
    def viewOrdersByMenu(self, menu_id):
        query = "SELECT * FROM orders WHERE menu_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (menu_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (menu_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()




# 8
    def viewOrdersByPayment(self, payment_id):
        query = "SELECT * FROM orders WHERE payment_id = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (payment_id)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (payment_id)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()


# 9
    def viewOrdersByDate(self, order_date):
        query = "SELECT * FROM orders WHERE order_date = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (order_date)
            # cursor        
            # cursor.execute(query, data)            
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (order_date)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:
            print(e)
            return False
        # finally:
        #     self.db.close()


# 10
    def viewOrdersByIsPaid(self, is_paid):
        query = "SELECT * FROM orders WHERE is_paid = %s"
        try:
            # cursor = self.db.get_cursor()
            # data = (is_paid)
            # cursor.execute(query, data)
            # if cursor.rowcount  == 0:
            #     return False
            # else:
            #     orders = cursor.fetchall()
            #     return orders
            with Database() as cursor:
                data = (is_paid)
                cursor.execute(query, data)
                if cursor.rowcount  == 0:
                    return False
                else:
                    orders = cursor.fetchall()
                    return orders
        except Exception as e:            
            print(e)
            return False
        # finally:
        #     self.db.close()




    