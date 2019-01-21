from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .factory.RuntimeSourceCreator import RuntimeSourceCreator

class CreatorLoader:

    def __init__(self):
        pass

    def load_factory(self, factory_name):
        
        factory_module = import_module('.RuntimeSourceCreator' + factory_name, 'runtime.creator.concrete')
        classes = getmembers(factory_module,
                            lambda m: isclass(m) and not isabstract(m))

        for name, _class in classes:
            if issubclass(_class, RuntimeSourceCreator):
                return _class()

