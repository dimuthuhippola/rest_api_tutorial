from flask import Flask
from flask_restful import Api

from resource.hello_get import HelloGet
from resource.hello_post import HelloPost

application = Flask(__name__)

api = Api(application)

api.add_resource(HelloGet, '/get/<string:data>')
api.add_resource(HelloPost, '/post')

if __name__ == '__main__':
    application.run(debug=True, port=3002)
