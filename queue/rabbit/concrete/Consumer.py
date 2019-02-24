from ..abstract.Rabbit import Rabbit
from ..Settings import no_ack

from requests import post,get
from settings import host_teaster, wait_for_teaster
import time

class Consumer(Rabbit):

    def publish(self, body):
        pass

    def consume(self, callback):
        self.channel.basic_consume(callback,
                                     queue=self.queue_name,
                                     no_ack=no_ack)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


    def callback(self, channel, method, properties, body):
        print(" [x] Received %r" % body)
        #channel.basic_ack(delivery_tag=method.delivery_tag)
        self.ack(delivery_tag=method.delivery_tag)
    
    @classmethod
    def register(cls, runenv, product, wait_for_teaster=False):
        
        def keepalive():
            while(True):
                try:
                    print(" [Consumer] sending keepalive to {}...".format(host_teaster))
                    r = get('http://{}:5000/keepalive'.format(host_teaster))
                    #r = get('http://localhost:5000/keepalive')
                    print("response keepalive \n{}".format(r.text))
                    break
                except Exception as error:
                        print(error)
                        print(" [Consumer] wait until teaster on {} is up and running...".format(host_teaster))
                        time.sleep(5)

        if wait_for_teaster: keepalive()
        
        print(" [Consumer] registering a consumer to teaster {}".format(host_teaster))
        r = post('http://{}:5000/consumers'.format(host_teaster), data={"runenv": runenv, "product": product})
        #r = post('http://localhost:5000/consumers', data={"runenv": runenv, "product": product})
        print(" [Consumer] response registration \n{}".format(r.text))
        return r.json()
        
