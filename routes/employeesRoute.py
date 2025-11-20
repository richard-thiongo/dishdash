from flask import Blueprint, request
from controllers.employeeController import EmployeesController

# Define the Blueprint for employee routes
employees_blueprint = Blueprint('employees', __name__, url_prefix='/employees')
employees_controller = EmployeesController()

# Route to create a new employee
@employees_blueprint.route('/create', methods=['POST'])
def create_employee():
    return employees_controller.createEmployee(request)

# Route to get all employees
@employees_blueprint.route('/view', methods=['POST'])
def view_employees():
    return employees_controller.viewEmployees(request)

@employees_blueprint.route('/view_department', methods=['POST'])
def view_employee_department():
    return employees_controller.viewEmployeeDepartment(request)

@employees_blueprint.route('/view_orders', methods=['POST'])
def view_employee_orders():
    return employees_controller.viewEmployeeOrders(request)

@employees_blueprint.route('/login', methods=['POST'])
def employee_login():
    return employees_controller.employeeeLogin(request)

@employees_blueprint.route('/profile', methods=['POST'])
def employee_profile():
    return employees_controller.employeeProfile(request)

@employees_blueprint.route('/update', methods=['POST'])
def update_employee_profile():
    return employees_controller.updateEmployeeProfile(request)

@employees_blueprint.route('/delete', methods=['DELETE'])
def delete_employee():
    return employees_controller.deleteEmployee(request)
