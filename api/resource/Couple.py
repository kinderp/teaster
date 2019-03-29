from flask_restful import Resource, Api, reqparse, fields

import os
import hashlib

from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit, wait_for_teaster
from queue.rabbit.concrete import Producer


class Couple(Resource):

    parser = reqparse.RequestParser()
    producer = Producer(**conn_details)
    
    def post(self, c_id):
        # put here the code for a producer.
        pass
