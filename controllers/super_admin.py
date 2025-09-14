from flask import jsonify, request
from services.super_admin import SuperAdminService
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt

class SuperAdminController:
    def __init__(self):
        self.super_admin_service = SuperAdminService()



    def createSuperAdmin(self, request):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        hashed_password = function.hash_password(password)
        result = self.super_admin_service.createSuperAdmin(username, hashed_password)
        if result:
            return jsonify({"message": "Super admin created successfully"}), 201
        else:
            return jsonify({"message": "Super admin creation failed"}), 500
        


    def superAdminLogin(self, request):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        result = self.super_admin_service.superAdminLogin(username, password)
        if not result:
            return jsonify({"message": "Super admin login failed"}), 500
        else:
            if "password" in result:
                del result["password"]
            role = "super_admin"
            access_token = create_access_token(identity = username, fresh = True, additional_claims = {"role": role})
            refresh_token = create_refresh_token(username)
            return jsonify({
                "message": "Super admin login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "super_admin": result
            }), 200