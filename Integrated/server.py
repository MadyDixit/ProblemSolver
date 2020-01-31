from flask import Flask, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self):
        return {'employee':[{'id':1,'name':'Madhav'},{'id':2,'name':'Aman'}]}

api.add_resource(Employee,'/employees')

if __name__ == '__main__':
    app.run(port=5002)