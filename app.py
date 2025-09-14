from flask import Flask 
from routes.companyRoute import companies_blueprint
from datetime import timedelta
from flask_jwt_extended import JWTManager   
from routes.employeesRoute import employees_blueprint
from routes.restaurantsRoutes import restaurants_blueprint
from routes.menuRoute import menus_blueprint
from routes.imageRoute import image_blueprint
from routes.ordersRoute import orders_blueprint
from routes.super_admin import super_admin_blueprint


app = Flask(__name__)

app.secret_key = "8540e7fe39a6b2b429a08d2c36c73b666327b7be222e0ca1e03def6604c7f23c"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=2)
jwt = JWTManager(app)


# Register the companies blueprint
app.register_blueprint(companies_blueprint)
app.register_blueprint(employees_blueprint)
app.register_blueprint(restaurants_blueprint)
app.register_blueprint(menus_blueprint)
app.register_blueprint(image_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(super_admin_blueprint)

if __name__ == '__main__':
    app.run(debug=True)