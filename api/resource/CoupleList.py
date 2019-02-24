from flask_restful import Resource, Api, reqparse, fields

from queue.rabbit.concrete import Producer
from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit
 
import json


class CoupleList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('provenv', required=True, help="A couple must specify the related provenv")
    parser.add_argument('cid', required=True, help="A couple must specify the taget consumer")
    
    def post(self):
       
        data = CoupleList.parser.parse_args()
        print("[CoupleList:post] arrived data: \n{}".format(json.dumps(data,indent=4, sort_keys=True)))
        
        #conn_details = {
        #    "host" :host_rabbit,
        #    "vhost" : vhost,
        #    "queue" : queue,
        #    "exchange" : exchange,
        #    "exchange_type" : exchange_type,
        #    "routing" : routing
        #}

        conn_details = {
            "host" : host_rabbit,
            "vhost" : vhost,
            "queue" : data['cid'],
            "exchange" : exchange,
            "exchange_type" : exchange_type,
            "routing" : data['cid'],
            "wait_for_rabbit": wait_for_rabbit
        }

        #import pdb
        #pdb.stack_trace()

        print("[CoupleList:post] producer, connecting to rabbit: \n{}".format(json.dumps(conn_details,indent=4, sort_keys=True)))
        p = Producer(**conn_details)
        p.publish(json.dumps(data))

        return {}

