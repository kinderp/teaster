from abc import ABCMeta, abstractmethod

class RuntimeSource:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def show(self):
        pass


