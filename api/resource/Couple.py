from flask_restful import Resource, Api, reqparse, fields

import os
import hashlib

class Couple(Resource):

    parser = reqparse.RequestParser()

    def post(self, c_id):
        # put here the code for producer.
        pass
