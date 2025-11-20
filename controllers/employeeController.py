from flask import jsonify
import functions
from services.employees import EmployeesService
import uuid
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt

class EmployeesController:
    def __init__(self):
        self.employees_service = EmployeesService()

    # create employee
    @jwt_required()
    def createEmployee(self, request):
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        company_id = data["company_id"]
        employee_email = data["employee_email"]
        employee_status = data["employee_status"]
        department_id = data["department_id"]
        profile_pic = data["profile_pic"]
        employee_password = data["employee_password"]
        claims = get_jwt()
        role = claims["role"]
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        hashed_password = functions.hash_password(employee_password)

        result = self.employees_service.createEmployee(first_name, last_name, employee_email, company_id, department_id, employee_status, profile_pic, hashed_password)
        if result:
            return jsonify({"message": "Employee added successfully"}), 201
        else:
            return jsonify({"message": "Employee addition failed"}), 500

    @jwt_required()
    def viewEmployees(self, request):
        data = request.get_json()
        company_id = data["company_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.employees_service.viewEmployees(company_id)
        if not result:
            return jsonify({"message": "No employees found"}), 404
        else:
            return jsonify({"employees": result}), 200

    @jwt_required()
    def viewEmployeeDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.employees_service.viewEmployeeDepartment(department_id)
        if not result:
            return jsonify({"message": "No employees found"}), 404
        else:
            return jsonify({"employees": result}), 200

    def employeeeLogin(self, request):
        data = request.get_json()
        employee_email = data["employee_email"]
        password = data["employee_password"]
        result = self.employees_service.employeeeLogin(employee_email, password)
        if not result:
            return jsonify({"message": "Login failed"}), 401
        else:
            if "password" in result:
                   del result["password"]
            access_token = create_access_token(identity = employee_email, fresh = True, additional_claims={"role": "employee"} )
            refresh_token = create_refresh_token(employee_email, additional_claims={"role": "employee"} )
            return jsonify({
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "employee": result
            }), 200

    def employeeProfile(self, request):
        data = request.get_json()
        employee_email = data["employee_email"]
        result = self.employees_service.employeeProfile(employee_email)
        if not result:
            return jsonify({"message": "Employee not found"}), 404
        else:
            if "password" in result:
                   del result["password"]
            return jsonify({"employee": result}), 200

    def updateEmployeeProfile(self, request):
        data = request.get_json()
        employee_id = data["employee_id"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        employee_email = data["employee_email"]
        department_id = data["department_id"]
        employee_status = data["employee_status"]
        profile_pic = data["profile_pic"]
        employee_password = data["employee_password"]
        claims = get_jwt()
        role = claims["role"]
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        hashed_password = functions.hash_password(employee_password)

        result = self.employees_service.updateEmployeeProfile(employee_id, first_name, last_name, employee_email, department_id, employee_status, profile_pic, hashed_password)
        if result:
            return jsonify({"message": "Employee updated successfully"}), 200
        else:
            return jsonify({"message": "Employee update failed"}), 500

    def deleteEmployee(self, request):
        data = request.get_json()
        employee_id = data["employee_id"]
        claims = get_jwt()
        role = claims["role"]
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401
        result = self.employees_service.deleteEmployee(employee_id)
        if result:
            return jsonify({"message": "Employee deleted successfully"}), 200
        else:
            return jsonify({"message": "Employee deletion failed"}), 500

    @jwt_required()
    def viewEmployeeOrders(self, request):
        data = request.get_json()
        employee_id = data["employee_id"]

        claims = get_jwt()
        role = claims["role"]

        # Only employeee role allowed
        if role != "employee":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.employees_service.viewEmployeeOrders(employee_id)

        if not result:
            return jsonify({"message": "No orders found for this employee"}), 404
        
        return jsonify({"orders": result}), 200