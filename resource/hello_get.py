from flask_restful import Resource


class HelloGet(Resource):
    def get(self, data):
        # data base query buisness aaa#
        return {
            'name': data,
            'age': 65
        }
