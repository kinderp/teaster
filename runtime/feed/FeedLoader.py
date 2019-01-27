from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .factory.RuntimeSourceFeed import RuntimeSourceFeed

class FeedLoader:

    def __init__(self):
        pass

    def load_feed(self, factory_name):
        factory_module = import_module('.RuntimeSourceFeed' + factory_name, 'runtime.feed.concrete')
        classes = getmembers(factory_module,
                            lambda m: isclass(m) and not isabstract(m))

        for name, _class in classes:
            if issubclass(_class, RuntimeSourceCreator):
                return _class()

