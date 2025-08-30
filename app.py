from flask import Flask 
from routes.companyRoute import companies_blueprint

app = Flask(__name__)
app.register_blueprint(companies_blueprint)

if __name__ == '__main__':
    app.run(debug=True)