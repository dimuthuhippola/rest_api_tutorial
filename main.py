from flask import Flask, jsonify
from flask_restful import Api
from db import db
from flask_jwt import JWT

from resource.get_user import GetUser
from resource.register_user import RegisterUser
from resource.insert_product import InsertProduct
from resource.mock_resource import MockAPI
from security import authenticate, identity

application = Flask(__name__)
application.secret_key = "MYSECRETKEY"

api = Api(application)
jwt = JWT(application, authenticate, identity)

application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dimuthuh:123_bumblebee@localhost:5432/rest_api_tutorial"

db.init_app(application)
with application.app_context():
    db.create_all()

api.add_resource(GetUser, '/findUser/<string:data>')
api.add_resource(RegisterUser, '/registerUser')
api.add_resource(InsertProduct, '/insertProduct')
api.add_resource(MockAPI, '/Mock')

if __name__ == '__main__':
    application.run(debug=True, port=3002)
