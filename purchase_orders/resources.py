from flask import Flask, jsonify
from flask_restful import Api, Resource

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items':
            [
                {
                    'id': 1,
                    'description': 'Item do pedido 1',
                    'price': 20.99
                }
            ]

    }
]


class PurchaseOrders(Resource):
    @staticmethod
    def get():
        return jsonify(purchase_orders)