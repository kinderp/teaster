from flask_restful import Resource, Api, reqparse, fields

from ..Database import consumer_list

import os
import hashlib

class Consumer(Resource):

    def get(self, c_id):
        if c_id in consumer_list:
            return consumer_list[c_id]
        else:
            return {"id": "None"}
