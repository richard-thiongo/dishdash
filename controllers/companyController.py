from flask import jsonify, request
import functions
from services.companies import CompanyService
import uuid
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, create_refresh_token

class CompanyController:
    def __init__(self):
        self.company_service = CompanyService()

    # Controller to create a company
    def createCompany(self, request):
        data = request.get_json()
        company_name = data["company_name"]
        company_address = data["company_address"]
        company_email = data["company_email"]
        company_phone = data["company_phone"]
        company_logo = data["company_logo"]
        password = data["password"]

        hashed_password = functions.hash_password(password)

        result = self.company_service.createCompany(
            company_name, company_address, company_email, company_phone, company_logo, hashed_password
        )
        if result:
            return jsonify({"message": "Company created successfully"}), 201
        else:
            return jsonify({"message": "Company creation failed"}), 500

    # Controller for company login
    def companyLogin(self, request):
        try:
            data = request.get_json()
            if not data or "company_email" not in data or "password" not in data:
                return jsonify({"message": "Missing email or password"}), 400

            email = data["company_email"]
            password = data["password"]

            result = self.company_service.companyLogin(email, password)
            if not result:
                return jsonify({"message": "Login failed: invalid credentials"}), 401

            # Remove password before returning
            result.pop("password", None)

            role = "company"
            access_token = create_access_token(identity=email, fresh=True, additional_claims={"role": role})
            refresh_token = create_refresh_token(identity=email)

            return jsonify({
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "company": result
            }), 200

        except Exception as e:
            print("Controller login error:", e)
            return jsonify({"message": "Internal server error"}), 500

    # Controller to get company profile
    @jwt_required()
    def companyProfile(self, request):
        data = request.get_json()
        company_id = data["company_id"]

        claims = get_jwt()
        role = claims.get("role")

        # Allow both company and employee roles
        if role not in ["company", "employee"]:
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.companyProfile(company_id)

        if not result:
            return jsonify({"message": "Company not found"}), 404

        result.pop("password", None)
        return jsonify({"company": result}), 200

    # Controller to create a department
    @jwt_required()
    def createDepartment(self, request):
        data = request.get_json()
        department_name = data["department_name"]
        company_id = data["company_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.createDepartment(department_name, company_id)
        if result:
            return jsonify({"message": "Department created successfully"}), 201
        else:
            return jsonify({"message": "Department creation failed"}), 500

    # Controller to get departments by company_id
    @jwt_required()
    def getDepartments(self, request):
        data = request.get_json()
        company_id = data["company_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.getDepartments(company_id)
        if not result:
            return jsonify({"message": "No departments found"}), 404
        else:
            return jsonify({"departments": result}), 200

    # Controller to update department
    @jwt_required()
    def updateDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]
        department_name = data["department_name"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.updateDepartment(department_id, department_name)
        if result:
            return jsonify({"message": "Department updated successfully"}), 200
        else:
            return jsonify({"message": "Department update failed"}), 500

    # Controller to delete department
    @jwt_required()
    def deleteDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.deleteDepartment(department_id)
        if result:
            return jsonify({"message": "Department deleted successfully"}), 200
        else:
            return jsonify({"message": "Department deletion failed"}), 500

    # Controller to get department by department_id
    @jwt_required()
    def getDepartmentById(self, request):
        data = request.get_json()
        department_id = data["department_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.getDepartmentById(department_id)
        if not result:
            return jsonify({"message": "Department not found"}), 404
        else:
            return jsonify({"department": result}), 200

    # Controller to count all departments
    @jwt_required()
    def countDepartments(self, request):
        data = request.get_json()
        company_id = data["company_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.countDepartments(company_id)
        if not result:
            return jsonify({"message": "No departments found"}), 404
        else:
            return jsonify({"count": result}), 200

    # Controller to get all employees by department_id
    @jwt_required()
    def getEmployeesByDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.getEmployeesByDepartment(department_id)
        if not result:
            return jsonify({"message": "No employees found"})
        else:
            return jsonify({"employees": result}), 200

    # Controller to count employees by department
    @jwt_required()
    def countEmployeesByDepartment(self, request):
        data = request.get_json()
        department_id = data["department_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.countEmployeesByDepartment(department_id)
        if not result:
            return jsonify({"message": "No employees found"}), 404
        else:
            return jsonify({"count": result}), 200

    # Controller to count all employees
    @jwt_required()
    def countAllEmployees(self, request):
        data = request.get_json()
        company_id = data["company_id"]

        claims = get_jwt()
        role = claims.get("role")
        if role != "company":
            return jsonify({"message": "Unauthorized"}), 401

        result = self.company_service.countAllEmployees(company_id)
        if not result:
            return jsonify({"message": "No employees found"}), 404
        else:
            return jsonify({"count": result}), 200