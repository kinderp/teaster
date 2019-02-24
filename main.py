from flask import Flask, request
from flask_restful import Api

from api.resource import KeepAlive
from api.resource import Consumer
from api.resource import ConsumerList
from api.resource import CoupleList

app = Flask(__name__)
api = Api(app)

api.add_resource(KeepAlive, '/keepalive')
api.add_resource(Consumer, '/consumer/<string:c_id>')
api.add_resource(ConsumerList, '/consumers')
api.add_resource(CoupleList, '/couples')

if __name__ == '__main__':

    app.run(debug=True,port=5000,host='0.0.0.0')

