from flask import jsonify
import functions
from services.companies import CompanyService
import uuid
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt_identity,  create_refresh_token

class CompanyController:
    def __init__(self):
        self.company_service = CompanyService()

    def createCompany(self, request):
            data = request.get_json()
            company_name = data["company_name"]
            company_address = data["company_address"]
            company_email = data["company_email"]
            company_phone = data["company_phone"]
            company_logo = data["company_logo"]
            password = data["password"]

            hashed_password = functions.hash_password(password)

            result = self.company_service.createCompany(company_name, company_address, company_email, company_phone, company_logo, hashed_password)
            if result:
                return jsonify({"message": "Company created successfully"}), 201
            else:
                return jsonify({"message": "Company creation failed"}), 500
            

    def companyLogin(self, request):
         data = request.get_json()
         email = data["company_email"]
         password = data["password"]
         result = self.company_service.companyLogin(email, password)
        #  print(result)
         if not result:
             return jsonify({"message": "Login failed"}), 401
         else:
             if "password" in result:
                   del result["password"]
             access_token = create_access_token(identity = email, fresh = True)
             refresh_token = create_refresh_token(email)
             return jsonify({
                 "message": "Login successful",
                 "access_token": access_token,
                 "refresh_token": refresh_token,
                 "company": result
             }), 200
     # Route to get company profile    
    @jwt_required()
    def companyProfile(self, request):
        data = request.get_json()
        company_id = data["company_id"]
        result = self.company_service.companyProfile(company_id)

        if not result:
            return jsonify({"message": "Company not found"}), 404
        else:
            if "password" in result:
                   del result["password"]
            return jsonify({"company": result}), 200
        
    # Route to create a new department
    @jwt_required()
    def createDepartment(self, request):
        data = request.get_json()
        department_name = data["department_name"]
        company_id = data["company_id"]

        result = self.company_service.createDepartment(department_name, company_id)
        print(result)
        if result:
            return jsonify({"message": "Department created successfully"}), 201
        else:
            return jsonify({"message": "Department creation failed"}), 500
        
    # Route to get departments by company_id
    @jwt_required()
    def getDepartments(self, request):
        data = request.get_json()
        company_id = data["company_id"]
        result = self.company_service.getDepartments(company_id)
        if not result:
            return jsonify({"message": "No departments found"}), 404
        else:
            return jsonify({"departments": result}), 200
        

    # Route to update department
    @jwt_required()
    def updateDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]
        department_name = data["department_name"]
        result = self.company_service.updateDepartment(department_id, department_name)
        if result:
            return jsonify({"message": "Department updated successfully"}), 200
        else:
            return jsonify({"message": "Department update failed"}), 500
        

    # Route to delete department
    @jwt_required()
    def deleteDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]
        result = self.company_service.deleteDepartment(department_id)
        if result:
            return jsonify({"message": "Department deleted successfully"}), 200
        else:
            return jsonify({"message": "Department deletion failed"}), 500


        
         
                
         


