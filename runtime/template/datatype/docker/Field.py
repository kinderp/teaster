from abc import ABCMeta, abstractproperty

class Field:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__description = None

    @abstractproperty
    def description(self):
        pass

