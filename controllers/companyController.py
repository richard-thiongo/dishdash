from flask import jsonify
from services.companies import CompanyService
import functions

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


