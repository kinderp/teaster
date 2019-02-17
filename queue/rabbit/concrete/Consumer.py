from ..abstract.Rabbit import Rabbit
from ..Settings import no_ack

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
        channel.basic_ack(delivery_tag=method.delivery_tag)


