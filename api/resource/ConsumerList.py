from flask_restful import Resource, Api, reqparse, fields

from ..Database import consumer_list

import os
import hashlib

class ConsumerList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('runenv', required=True, help="A consumer must specify the related runenv")
    parser.add_argument('product', required=True, help="A consumer must specify the known product")
    
    def get(self):
        return consumer_list

    def post(self):
        c_id = hashlib.sha256(os.urandom(1024)).hexdigest()
        data = ConsumerList.parser.parse_args()
        new_consumer = {"id": c_id, "runenv": data["runenv"], "product": data["product"]}
        consumer_list[c_id] = new_consumer
        return new_consumer

