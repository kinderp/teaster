from queue.rabbit.concrete import Producer
import json
import time

conn_details = {
        "host" :'rabbit', 
        "vhost" : None,
        "queue" : 'test', 
        "exchange" : 'test', 
        "exchange_type" : 'direct', 
        "routing" : 'test'
}

# docker-compose doesn't garantee anything about services startup order
# so wait until rabbirmq connection is available

#import pika
#import time
#
#while(True):
#    try:
#
#        if conn_details['vhost'] is None:
#            connection = pika.BlockingConnection(pika.ConnectionParameters(conn_details['host']))
#        else:
#            connection = pika.BlockingConnection(pika.ConnectionParameters(host=conn_details['host'],virtual_host=conn_details['vhost']))
#        
#        if connection.is_open:
#            print('OK, rabbitmq is ready. Closing this connection and starting producer!')
#            connection.close()
#            break
#        else:
#            print("wait until rabbimq is up and running...")
#            time.sleep(5)
#
#    except Exception as error:
#        print("wait until rabbimq is up and running...")
#        time.sleep(5)
#
#p = Producer(host = 'rabbit', queue='test', exchange='test', exchange_type='direct', routing='test')

p = Producer(**conn_details)

message = {
    "one": 1,
    "two": 2
}

while(True):
    p.publish(json.dumps(message))
    time.sleep(3)

