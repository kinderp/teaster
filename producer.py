from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit, wait_for_teaster
from queue.rabbit.concrete import Producer
import json
import time

conn_details = {
        "host" :host_rabbit, 
        "vhost" : vhost,
        "queue" : queue, 
        "exchange" : exchange, 
        "exchange_type" : exchange_type, 
        "routing" : routing,
        "wait_for_rabbit": wait_for_rabbit
}

# docker-compose doesn't garantee anything about services startup order
# so wait until rabbirmq connection is available

p = Producer(**conn_details)

message = {
    "one": 1,
    "two": 2
}

while(True):
    p.publish(json.dumps(message))
    time.sleep(3)

