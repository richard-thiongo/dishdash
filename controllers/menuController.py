from flask import jsonify
import functions
from services.menu import MenusService
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="dzwituw4t",
    api_key="897437964615358",
    api_secret="_Wk3jS5lJRXlHa2uN2ejVwC5L60",
    secure=True
)





class MenusController:
    def __init__(self):
        self.menus_service = MenusService()


    @jwt_required()
    def createMenu(self, request):
        try:
            menu_name = request.form.get("menu_name")
            menu_description = request.form.get("menu_description")
            menu_price = request.form.get("menu_price")
            menu_status = request.form.get("menu_status")
            restaurant_id = request.form.get("restaurant_id")
            menu_photo = request.files.get("menu_photo")
            category = request.form.get("category")

            print("Cloudinary API key:", cloudinary.config().api_key)
            print("File received:", menu_photo)

            if not menu_photo:
                return jsonify({"message": "No image received"}), 400

            upload_result = cloudinary.uploader.upload(menu_photo)
            image_url = upload_result.get("secure_url")

            result = self.menus_service.createMenu(
                menu_name, menu_description, menu_price,
                image_url, menu_status, restaurant_id, category
            )

            if result:
                return jsonify({"message": "Meal added successfully", "image_url": image_url}), 201
            else:
                return jsonify({"message": "Meal addition failed"}), 400

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": str(e)}), 500
        
            

    
    def viewMenu(self, request):
        data = request.get_json()
        restaurant_id = data["restaurant_id"]
        result = self.menus_service.viewMenu(restaurant_id) 
        if not result:
            return jsonify({"message": "No meals found"}), 404
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
            return jsonify({"message": "Meal updated successfully"}), 200
        else:
            return jsonify({"message": "Meal updated failed"}), 500  
        


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
            return jsonify({"message": "Meal deleted successfully"}), 200
        else:
            return jsonify({"message": "Meal deletion failed"}), 500
        


   
    def viewMenuById(self, request):
        data = request.get_json()
        menu_id = data["menu_id"]
        result = self.menus_service.viewMenuById(menu_id)
        if not result:
            return jsonify({"message": "Meal not found"}), 404
        else:
            return jsonify({"menu": result}), 200
        


    # View all menu
    def viewAllMenu(self, request):
        result = self.menus_service.viewAllMenus()
        if not result:
            return jsonify({"message": "No meals found"}), 404
        else:
            return jsonify({"menus": result}), 200