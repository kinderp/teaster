from queue.rabbit.concrete import Consumer
import json

from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit, wait_for_teaster

# docker-compose doesn't garantee anything about services startup order
# so wait until rabbirmq connection is available

result = Consumer.register('docker','ubuntu', wait_for_teaster)

print("registration result \n{}".format(json.dumps(result, indent=4, sort_keys=True)))

queue = result['id']
routing = queue

#print("queue: {}".format(queue))

conn_details = {
        "host" :host_rabbit, 
        "vhost" : vhost,
        "queue" : queue, 
        "exchange" : exchange, 
        "exchange_type" : exchange_type, 
        "routing" : routing,
        "wait_for_rabbit": wait_for_rabbit
}

print("producer, connecting to rabbit: \n{}".format(json.dumps(conn_details,indent=4, sort_keys=True)))

p = Consumer(**conn_details)

p.consume(p.callback)

