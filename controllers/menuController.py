from flask import jsonify
import functions
from services.menu import MenusService
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt

class MenusController:
    def __init__(self):
        self.menus_service = MenusService()

    @jwt_required()
    def createMenu(self, request):
        data = request.get_json()
        menu_name = data["menu_name"]
        menu_description = data["menu_description"]
        menu_price = data["menu_price"]
        menu_photo = data["menu_photo"]
        menu_status = data["menu_status"]
        restaurant_id = data["restaurant_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.menus_service.createMenu(menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id)
        if result:
            return jsonify({"message": "Menu created successfully"}), 201
        else:
            return jsonify({"message": "Menu creation failed"}), 400
        

    @jwt_required()
    def viewMenu(self, request):
        data = request.get_json()
        restaurant_id = data["restaurant_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.menus_service.viewMenu(restaurant_id) 
        if not result:
            return jsonify({"message": "No menus found"}), 404
        else:
            return jsonify({"menus": result}), 200  
        


    @jwt_required()
    def updateMenu(self, request):
        data = request.get_json()
        menu_id = data["menu_id"]
        menu_name = data["menu_name"]
        menu_description = data["menu_description"]
        menu_price = data["menu_price"]
        menu_photo = data["menu_photo"]
        menu_status = data["menu_status"]
        restaurant_id = data["restaurant_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.menus_service.updateMenu(menu_id, menu_name, menu_description, menu_price, menu_photo, menu_status, restaurant_id)
        if result:
            return jsonify({"message": "Menu updated successfully"}), 200
        else:
            return jsonify({"message": "Menu update failed"}), 500  
        


    @jwt_required()
    def deleteMenu(self, request):
        data = request.get_json()
        menu_id = data["menu_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.menus_service.deleteMenu(menu_id)
        if result:
            return jsonify({"message": "Menu deleted successfully"}), 200
        else:
            return jsonify({"message": "Menu deletion failed"}), 500
        


    @jwt_required()
    def viewMenuById(self, request):
        data = request.get_json()
        menu_id = data["menu_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "restaurant":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.menus_service.viewMenuById(menu_id)
        if not result:
            return jsonify({"message": "Menu not found"}), 404
        else:
            return jsonify({"menu": result}), 200