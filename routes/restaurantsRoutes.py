from flask import Blueprint, request
from controllers.restaurantsController import RestaurantsController

# Define the Blueprint for restaurant routes
restaurants_blueprint = Blueprint('restaurants', __name__, url_prefix='/restaurants')
restaurants_controller = RestaurantsController()

# Route to create a new restaurant
@restaurants_blueprint.route('/create', methods=['POST'])
def create_restaurant():
    return restaurants_controller.createRestaurant(request)

# Route to login a restaurant
@restaurants_blueprint.route('/login', methods=['POST'])
def restaurant_login():
    return restaurants_controller.restaurantLogin(request)

# Route to get restaurant profile
@restaurants_blueprint.route('/profile', methods=['POST'])
def restaurant_profile():
    return restaurants_controller.restaurantProfile(request)

# Route to update restaurant profile    
@restaurants_blueprint.route('/update', methods=['POST'])
def update_restaurant():
    return restaurants_controller.updateRestaurant(request)

# Route to delete restaurant
@restaurants_blueprint.route('/delete', methods=['DELETE'])
def delete_restaurant():
    return restaurants_controller.deleteRestaurant(request)

# Route to view all restaurants
@restaurants_blueprint.route('/view', methods=['GET'])
def view_restaurants():
    return restaurants_controller.viewRestaurants()




# Route to get total orders of a restaurant
@restaurants_blueprint.route('/total-orders', methods=['POST'])
def total_orders():
    return restaurants_controller.getTotalOrders(request)



@restaurants_blueprint.route('/restaurant/<string:restaurant_id>', methods=['GET'])
def get_restaurant_orders(restaurant_id):
    return restaurants_controller.viewOrdersByRestaurant(restaurant_id)

