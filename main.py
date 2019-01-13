from flask import Flask
from flask import request
import json

app = Flask(__name__)

"""
curl -H "Content-Type: application/json" POST -d \
'{"id":1003, "action":"like", "user":"a.caristia@gmail.com", "type":"news"}' \
http://localhost:5002/
"""

@app.route("/", methods=['POST'])
def hello():
    #data = json.loads(request.data.decode('utf-8'))
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    return "Hello World!"

if __name__ == '__main__':

    app.run(debug=False,port=5000,host='0.0.0.0')

