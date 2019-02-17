import pika

from ..Settings import delivery_mode
from ..abstract.Rabbit import Rabbit

class Producer(Rabbit):

    def consume(self, callback):
        pass

    def publish(self, body):
        if self.channel:
            self.channel.basic_publish(exchange=self.exchange_name,
                                         routing_key=self.routing_key,
                                         body=body,
                                         properties=pika.BasicProperties(
                                            delivery_mode=delivery_mode,  # make message persistent
                                         ))

            print(' [*] Published message: {}'.format(body))
