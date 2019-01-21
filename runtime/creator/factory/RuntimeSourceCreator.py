from abc import ABCMeta, abstractmethod

class RuntimeSourceCreator:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create(self):
        pass




