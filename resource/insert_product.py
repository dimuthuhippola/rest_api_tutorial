from flask_restful import Resource
from flask import request
from models.products import Products
from flask_jwt import jwt_required, current_identity

class InsertProduct(Resource):

    @jwt_required()
    def post(self):

        if current_identity.user_name != 'dimuthuh':
            return 'Unauthorized', 401
        data = request.get_json()
        product = Products(product_name=data['product_name'], product_code=data['product_code'])
        product.save_product()
        return "product successfully saved", 201


