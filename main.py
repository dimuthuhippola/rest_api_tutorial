from flask import Flask
from flask_restful import Api
from db import db

from resource.hello_get import HelloGet
from resource.hello_post import HelloPost
import os

application = Flask(__name__)

api = Api(application)

application.config['SQLALCHEMY_DATABASE_URI']= os.environ['rest_api_tutorial_db_url']


db.init_app(application)
with application.app_context():
    db.create_all()

api.add_resource(HelloGet, '/findUser/<string:data>')
api.add_resource(HelloPost, '/post')

if __name__ == '__main__':
    application.run(debug=True, port=3002)
