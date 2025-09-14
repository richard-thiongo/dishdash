from flask import jsonify
import functions
from services.orders import OrdersService
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt

class OrdersController:
    def __init__(self):
        self.orders_service = OrdersService()


# 1
    @jwt_required
    def createOrder(self, request):
        data= request.get_json()
        payment_id = data["payment_id"]
        order_date = data["order_date"]
        is_paid = data["is_paid"]
        menu_id = data["menu_id"]
        employee_id = data["employee_id"]
        menu_price = data["menu_price"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.createOrder(payment_id, order_date, is_paid, menu_id, employee_id, menu_price)
        if result:
            return jsonify({"message": "Order created successfully"}), 201
        else:
            return jsonify({"message": "Order creation failed"}), 500
        

# 2
    @jwt_required
    def viewOrders(self):
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrders()
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        


# 3
    @jwt_required
    def viewOrderById(self, request):
        data = request.get_json()
        order_id = data["order_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrderById(order_id)
        if not result:
            return jsonify({"message": "Order not found"}), 404
        else:
            return jsonify({"order": result}), 200
        


# 4
    @jwt_required
    def deleteOrder(self, request):
        data = request.get_json()
        order_id = data["order_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.deleteOrder(order_id)
        if result:
            return jsonify({"message": "Order deleted successfully"}), 200
        else:
            return jsonify({"message": "Order deletion failed"}), 500
        



# 5
    @jwt_required
    def updateOrder(self, request):
        data = request.get_json()
        order_id = data["order_id"]
        payment_id = data["payment_id"]
        order_date = data["order_date"]
        is_paid = data["is_paid"]
        menu_id = data["menu_id"]
        employee_id = data["employee_id"]
        menu_price = data["menu_price"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.updateOrder(order_id, payment_id, order_date, is_paid, menu_id, employee_id, menu_price)
        if result:
            return jsonify({"message": "Order updated successfully"}), 200
        else:
            return jsonify({"message": "Order update failed"}), 500
        



# 6
    @jwt_required
    def viewOrdersByEmployee(self, request):
        data = request.get_json()
        employee_id = data["employee_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrdersByEmployee(employee_id)
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        


# 7
    @jwt_required
    def viewOrdersByMenu(self, request):
        data = request.get_json()
        menu_id = data["menu_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrdersByMenu(menu_id)
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        


# 8
    @jwt_required
    def viewOrdersByPayment(self, request):
        data = request.get_json()
        payment_id = data["payment_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrdersByPayment(payment_id)
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        


# 9
    @jwt_required
    def viewOrdersByStatus(self, request):
        data = request.get_json()
        is_paid = data["is_paid"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrdersByIsPaid(
            is_paid
        )
        (is_paid)
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        


# 10
    @jwt_required
    def viewOrdersByDate(self, request):
        data = request.get_json()
        order_date = data["order_date"]
        claims = get_jwt()
        role = claims["role"]
        if role != {"employee, company"}:
            return jsonify({"message": "Unauthorized"}), 401
        result = self.orders_service.viewOrdersByDate(order_date)
        if not result:
            return jsonify({"message": "No orders found"}), 404
        else:
            return jsonify({"orders": result}), 200
        






 