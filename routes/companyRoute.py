from flask import Blueprint, request
from controllers.companyController import CompanyController


# Define the Blueprint for company routes
companies_blueprint = Blueprint('companies', __name__, url_prefix='/companies')
companies_controller = CompanyController()

# Route to create a new company
@companies_blueprint.route('/create', methods=['POST'])
def create_company():
    return companies_controller.createCompany(request)
# Route for company login
@companies_blueprint.route('/login', methods=['POST'])
def company_login():
    return companies_controller.companyLogin(request)

# Route to get company profile
@companies_blueprint.route('/profile', methods=['POST'])
def company_profile():
    return companies_controller.companyProfile(request)

# Route to create a new department
@companies_blueprint.route('/department/create', methods=['POST'])
def create_department():
    return companies_controller.createDepartment(request)   

# Route to get departments by company_id
@companies_blueprint.route('/departments', methods=['POST'])
def get_departments():
    return companies_controller.getDepartments(request)


# Route to update a department
@companies_blueprint.route('/department/update', methods=['POST'])
def update_department():
    return companies_controller.updateDepartment(request)

# Route to delete a department
@companies_blueprint.route('/department/delete', methods=['POST'])
def delete_department():
    return companies_controller.deleteDepartment(request)




