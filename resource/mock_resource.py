from random import random
from flask_restful import Resource


class MockAPI(Resource):

    def get(self):
        words = ("Banana", "Grapes", "Mango", "Apple", "Orange", "Pineapple", "")
        return [
            {"serial": round(1000000*random()), "item": item} for item in words
        ]
