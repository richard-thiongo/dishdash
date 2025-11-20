from flask import Blueprint, request
from controllers.ordersController import OrdersController

orders_blueprint = Blueprint('orders', __name__, url_prefix='/orders')
orders_controller = OrdersController()

# CRUD ROUTES
@orders_blueprint.route('/create', methods=['POST'])
def create_order():
    return orders_controller.createOrder(request)

@orders_blueprint.route('/view', methods=['GET'])
def view_orders():
    return orders_controller.viewOrders()

@orders_blueprint.route('/viewById', methods=['POST'])
def view_order_by_id():
    return orders_controller.viewOrderById(request)

@orders_blueprint.route('/delete', methods=['DELETE'])
def delete_order():
    return orders_controller.deleteOrder(request)

@orders_blueprint.route('/update', methods=['PUT'])
def update_order():
    return orders_controller.updateOrder(request)

@orders_blueprint.route('/viewByEmployee', methods=['POST'])
def view_orders_by_employee():
    return orders_controller.viewOrdersByEmployee(request)

@orders_blueprint.route('/viewByMenu', methods=['POST'])
def view_orders_by_menu():
    return orders_controller.viewOrdersByMenu(request)

@orders_blueprint.route('/viewByPayment', methods=['POST'])
def view_orders_by_payment():
    return orders_controller.viewOrdersByPayment(request)

@orders_blueprint.route('/viewByStatus', methods=['POST'])
def view_orders_by_status():
    return orders_controller.viewOrdersByStatus(request)

@orders_blueprint.route('/viewByDate', methods=['POST'])
def view_orders_by_date():
    return orders_controller.viewOrdersByDate(request)

@orders_blueprint.route('/restaurant/<string:restaurant_id>', methods=['GET'])
def get_restaurant_orders(restaurant_id):
    return orders_controller.view_orders_by_restaurant(restaurant_id)
