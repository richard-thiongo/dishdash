from flask import Blueprint, request
from controllers.companyController import CompanyController

# Define the Blueprint for company routes
companies_blueprint = Blueprint('companies', __name__, url_prefix='/companies')
companies_controller = CompanyController()

# Route to create a new company
@companies_blueprint.route('/create', methods=['POST'])
def create_company():
    return companies_controller.createCompany(request)

