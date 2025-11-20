from flask import jsonify
import functions
from services.restaurants import RestaurantsService
import uuid
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt_identity,  create_refresh_token, get_jwt
from functions import hash_password, hash_verify

class RestaurantsController:
    def __init__(self):
        self.restaurants_service = RestaurantsService()


    def createRestaurant(self, request):
        data = request.get_json()
        restaurant_name = data["restaurant_name"]
        restaurant_address = data["restaurant_address"]
        restaurant_email = data["restaurant_email"]
        till_no = data["till_no"]
        restaurant_description = data["restaurant_description"]
        restaurant_status = data["restaurant_status"]
        restaurant_password = data["restaurant_password"]

        hashed_password = functions.hash_password(restaurant_password)

        result = self.restaurants_service.createRestaurant(restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, hashed_password)
        if result:
            return jsonify({"message": "Restaurant created successfully"}), 200
        else:
            return jsonify({"message": "Restaurant creation failed"}), 500
        


    def restaurantLogin(self, request):
        data = request.get_json()
        restaurant_email = data["restaurant_email"]
        restaurant_password = data["restaurant_password"]

        result = self.restaurants_service.restaurantLogin(restaurant_email, restaurant_password)
        if not result:
            return jsonify({"message": "Restaurant login failed"}), 500
        else:
            if "password" in result:
                del result["password"]

            role = "restaurant"
            access_token = create_access_token(identity = restaurant_email, fresh = True, additional_claims={"role": role} )
            refresh_token = create_refresh_token(restaurant_email)
            return jsonify({
                "message": "Restaurant login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "restaurant": result
            }), 200
           
        


    @jwt_required()
    def restaurantProfile(self, request):
        data = request.get_json()
        restaurant_id = data["restaurant_id"]
        claims = get_jwt
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.restaurants_service.restaurantProfile(restaurant_id)
        if  not result:
            return jsonify({"message": "Restaurant profile retrieval failed"}), 500
        else:
            if "password" in result:
                del result["password"]
            return jsonify({"restaurant": result}), 200
           
        

    @jwt_required()
    def updateRestaurant(self, request):
        data = request.get_json()
        restaurant_id = data["restaurant_id"]
        restaurant_name = data["restaurant_name"]
        restaurant_address = data["restaurant_address"]
        restaurant_email = data["restaurant_email"]
        till_no = data["till_no"]
        restaurant_description = data["restaurant_description"]
        restaurant_status = data["restaurant_status"]
        restaurant_password = data["restaurant_password"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        hashed_password = functions.hash_password(restaurant_password)

        result = self.restaurants_service.updateRestaurant(restaurant_id, restaurant_name, restaurant_address, restaurant_email, till_no, restaurant_description, restaurant_status, hashed_password)
        if result:
            return jsonify({"message": "Restaurant updated successfully"}), 200
        else:
            return jsonify({"message": "Restaurant update failed"}), 500
        


    @jwt_required()
    def deleteRestaurant(self, request):
        data = request.get_json()
        restaurant_id = data["restaurant_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.restaurants_service.deleteRestaurant(restaurant_id)
        if result:
            return jsonify({"message": "Restaurant deleted successfully"}), 200
        else:
            return jsonify({"message": "Restaurant deletion failed"}), 500
        


    def viewRestaurants(self ):
        result = self.restaurants_service.viewRestaurants()
        if not result:
            return jsonify({"message": "Restaurants retrieval failed"}), 500
        else:
            return jsonify({"restaurants": result}), 200




    @jwt_required()
    def getTotalOrders(self, request):
        data = request.get_json()
        restaurant_id = data.get("restaurant_id")
    
        claims = get_jwt()
        role = claims.get("role")
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
    
        total_orders = self.restaurants_service.totalOrders(restaurant_id)
        return jsonify({"total_orders": total_orders}), 200



    @jwt_required()
    def viewOrdersByRestaurant(self, restaurant_id):
        claims = get_jwt()
        role = claims["role"]

        # You can adjust the condition depending on your roles
        if role not in ["restaurant", "admin", "company", "employee"]:
            return jsonify({"message": "Unauthorized"}), 401

        result = self.restaurants_service.viewOrdersByRestaurant(restaurant_id)

        if not result:
            return jsonify({"message": "No orders found"}), 404

        return jsonify({"orders": result}), 200