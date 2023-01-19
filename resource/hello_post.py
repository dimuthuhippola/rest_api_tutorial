from flask_restful import Resource
from flask import request
from models.users import Users


class HelloPost(Resource):
    def post(self):
        data = request.get_json()

        user = Users(user_name=data['user_name'], emp_name=data['emp_name'], pass_word=data['pass_word'])
        user.save_user()

        return f'successfully added user {user.emp_name}', 201
