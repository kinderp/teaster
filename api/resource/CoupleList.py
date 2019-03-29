from flask_restful import Resource, Api, reqparse, fields

from queue.rabbit.concrete import Producer
from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit
 
import json

from flask import request

class CoupleList(Resource):
    
    def post(self):
      
        data = request.get_json()
        print("[CoupleList:post] arrived data: \n{}".format(json.dumps(data,indent=4, sort_keys=True)))
        
        conn_details = {
            "host" : host_rabbit,
            "vhost" : vhost,
            "queue" : data['id'],
            "exchange" : exchange,
            "exchange_type" : exchange_type,
            "routing" : data['id'],
            "wait_for_rabbit": wait_for_rabbit
        }

        print("[CoupleList:post] producer, connecting to rabbit: \n{}".format(json.dumps(conn_details,indent=4, sort_keys=True)))
        p = Producer(**conn_details)
        p.publish(json.dumps(data))

        return {}

