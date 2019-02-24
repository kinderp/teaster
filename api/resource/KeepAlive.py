from flask_restful import Resource, Api, reqparse, fields

class KeepAlive(Resource):

    def get(self):
        return {} 
