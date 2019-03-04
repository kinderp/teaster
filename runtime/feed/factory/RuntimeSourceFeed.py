from abc import ABCMeta, abstractmethod

class RuntimeSourceFeed:
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, kwargs):
        pass

    @abstractmethod
    def parse_low(self, kwargs):
        pass

    @abstractmethod
    def to_dict(self):
        pass
