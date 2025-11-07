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
from routes.paymentRoute import payment_blueprint
from flask_cors import CORS



app = Flask(__name__)

# Allow all origins for testing
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Explicitly tell Flask which headers are allowed
app.config["CORS_HEADERS"] = ["Content-Type", "Authorization"]



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
app.register_blueprint(payment_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001)