from abc import ABCMeta, abstractproperty

class RuntimeSourceTemplate:
    __metaclass__ = ABCMeta

    @abstractproperty
    def template(self):
        pass



