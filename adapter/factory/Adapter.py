from abc import ABCMeta, abstractmethod
from runtime.creator import CreatorLoader
from runtime.feed import FeedLoader
from runtime.template import TemplateLoader

class Adapter:
    __metaclass__ = ABCMeta

    def __init__(self, **adaptee):
        self.__adaptee = adaptee
        self.__cloader = CreatorLoader()
        self.__floader = FeedLoader()
        self.__tloader = TemplateLoader()

    @property
    def adaptee(self):
        return self.__adaptee

    @property
    def cloader(self):
        return self.__cloader

    @property
    def floader(self):
        return self.__floader

    @property
    def tloader(self):
        return self.__tloader

    @property
    def tloader(self):
        return self.__tloader

    @abstractmethod
    def create(self):
        pass
