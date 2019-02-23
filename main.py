from flask import Flask, request
from flask_restful import Api

from api.resource import Consumer
from api.resource import ConsumerList
from api.resource import CoupleList

#from adapter.concrete import AdapterDocker

app = Flask(__name__)
api = Api(app)

api.add_resource(Consumer, '/consumer/<string:c_id>')
api.add_resource(ConsumerList, '/consumers')
api.add_resource(CoupleList, '/couples')

#"""
#curl -H "Content-Type: application/json" POST -d \
#'{"id":1003, "action":"like", "user":"a.caristia@gmail.com", "type":"news"}' \
#http://localhost:5002/
#"""
#
#@app.route("/", methods=['POST'])
#def hello():
#    #data = json.loads(request.data.decode('utf-8'))
#    data = json.loads(request.data.decode('utf-8'))
#    print(data)
#    return "Hello World!"
#
#@app.route("/delete_me", methods=['POST'])
#def delete_me():
#    data = json.loads(request.data.decode('utf-8'))
#    print(data)
#
#    runtime_soucre = AdaperDocker(data).create()
#    return "Hello World!"
#

if __name__ == '__main__':

    app.run(debug=True,port=5000,host='0.0.0.0')

