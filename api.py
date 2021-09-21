from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify, request

app = Flask(__name__)
api = Api(app)

class TransactionsController(Resource):
    def get(self):

        # startDate = request.args['startDate']
        # print(startDate)
        # endDate = request.args['endDate']
        # print(endDate)
        return {'hello': 'world'}

api.add_resource(TransactionsController, '/transactions/all')

if __name__ == '__main__':
    app.run(debug=True)