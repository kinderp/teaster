from abc import ABCMeta, abstractmethod

#from runtime.feed.factory import RuntimeSourceFeed
#from runtime.template.factory import RuntimeSourceTemplate

class RuntimeSourceCreator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, source_feed, source_template):
        pass




