from random import random

from flask_restful import Resource


class MockAPI(Resource):
    WORDS = ("Banana", "Grapes", "Mango", "Apple", "Orange", "Pineapple", "")

    def get(self):
        words = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
        return [
            {"serial": round(1000000*random()), "item": item} for item in words
        ]
