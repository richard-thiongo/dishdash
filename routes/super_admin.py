from flask import Blueprint, request
from controllers.super_admin import SuperAdminController

# Define the Blueprint for super admin routes
super_admin_blueprint = Blueprint('super_admin', __name__, url_prefix='/super_admin')
super_admin_controller = SuperAdminController()

# Route to create a new super admin
@super_admin_blueprint.route('/create', methods=['POST'])
def create_super_admin():
    return super_admin_controller.createSuperAdmin(request)

# Route to login a super admin
@super_admin_blueprint.route('/login', methods=['POST'])
def super_admin_login():
    return super_admin_controller.superAdminLogin(request)