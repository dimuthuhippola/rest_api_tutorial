from flask_restful import Resource
from flask import request


class HelloPost(Resource):
    def post(self):
        data = request.get_json()

        if data['Name'] == 'Dimuthu':
            return 'Yes'

        return 'No'
