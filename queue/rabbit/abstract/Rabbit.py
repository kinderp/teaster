from abc import ABCMeta, abstractmethod
import pika

from ..Settings import no_ack
from ..Settings import delivery_mode
from ..Settings import durable_queue

class Rabbit:
    __metaclass__ = ABCMeta
    
    def __init__(self,host="localhost", vhost=None, queue=None, exchange='', exchange_type='direct', routing=''):
        self.__connection = None
        self.__channel = None


        self.__no_ack = no_ack
        self.__delivery_mode = delivery_mode
        self.__host = host
        self.__vhost = vhost

        self.__queue_name = queue
        self.__queue = None
        self.__exchange_name = exchange
        self.__exchange_type = exchange_type
        self.__routing_key = routing

        self.connect()
        self.exchange()
        self.queue()

    @property
    def host(self):
        return self.__host

    @property
    def vhost(self):
        return self.__vhost

    @property
    def channel(self):
        return self.__channel

    @property
    def exchange_name(self):
        return self.__exchange_name

    @property
    def routing_key(self):
        return self.__routing_key

    @property
    def queue_name(self):
        return self.__queue_name

    def connect(self):
        if self.__vhost is None:
            self.__connection = pika.BlockingConnection(pika.ConnectionParameters(self.__host))
        else:
            self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.__host,virtual_host=self.__vhost))

        self.__channel = self.__connection.channel()

    def disconnect(self):
        self.__connection.close()

    def exchange(self):
        if self.__channel:
            self.__channel.exchange_declare(exchange=self.__exchange_name, exchange_type=self.__exchange_type)
    
    def queue(self):
        if self.__channel:
            self.__queue = self.__channel.queue_declare(queue=self.__queue_name,durable=durable_queue)
            self.__channel.queue_bind(exchange=self.__exchange_name, queue=self.__queue_name, routing_key=self.__routing_key)

    @abstractmethod
    def publish(self, body):
        pass

    @abstractmethod
    def consume(self, callback):
        pass

    def ack(self, delivery_tag, multiple=True):
        if self.__channel:
            self.__channel.basic_ack(delivery_tag, multiple=multiple)

    def nack(self, delivery_tag, multiple=True, requeue=True):
        if self.__channel:
            self.__channel.basic_nack(delivery_tag, multiple=multiple, requeue=requeue)

    def check_connection(self):
        if self.__connection:
            return self.__connection.is_open

