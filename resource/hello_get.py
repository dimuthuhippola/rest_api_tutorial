from flask_restful import Resource
from models.users import Users


class HelloGet(Resource):
    def get(self, data):
        user = Users.find_by_user_name(user_name=data)
        # data base query buisness aaa#

        return {
            'name': user.emp_name,
            'pass_word': user.pass_word
        }
