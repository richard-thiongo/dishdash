from flask import Blueprint, request
from controllers.menuController import MenusController

# Define the Blueprint for menu routes
menus_blueprint = Blueprint('menus', __name__, url_prefix='/menus')
menus_controller = MenusController()

# Route to create a new menu
@menus_blueprint.route('/create', methods=['POST'])
def create_menu():
    return menus_controller.createMenu(request)

# Route to view all menus
@menus_blueprint.route('/view', methods=['POST'])
def view_menus():
    return menus_controller.viewMenu(request)

# Route to update a menu
@menus_blueprint.route('/update', methods=['POST'])
def update_menu():
    return menus_controller.updateMenu(request)

# Route to delete a menu
@menus_blueprint.route('/delete', methods=['DELETE'])
def delete_menu():
    return menus_controller.deleteMenu(request)

# Route to view a menu by id
@menus_blueprint.route('/viewById', methods=['POST'])
def view_menu_by_id():
    return menus_controller.viewMenuById(request)