from abc import ABCMeta, abstractmethod, abstractproperty

class RuntimeSource:
    __metaclass__ = ABCMeta
    
    @abstractproperty
    def source(self):
        pass

    @abstractmethod
    def show(self):
        pass


