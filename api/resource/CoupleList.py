from flask_restful import Resource, Api, reqparse, fields

from queue.rabbit.concrete import Producer

import json

class CoupleList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('provenv', required=True, help="A couple must specify the related provenv")
    parser.add_argument('cid', required=True, help="A couple must specify the taget consumer")
    
    def get(self):
        return consumer_list

    def post(self):
        
        data = CoupleList.parser.parse_args()
        
        conn_details = {
            "host" :'rabbit',
            "vhost" : None,
            "queue" : data['cid'],
            "exchange" : 'test',
            "exchange_type" : 'direct',
            "routing" : 'test'
        }

        
        p = Producer(**conn_details)
        p.publish(json.dumps(data))

        return {}

