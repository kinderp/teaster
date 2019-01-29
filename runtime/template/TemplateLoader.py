from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .factory.RuntimeSourceTemplate import RuntimeSourceTemplate

class TemplateLoader:

    def __init__(self):
        pass

    def load_template(self, template_name):
        
        factory_module = import_module('.RuntimeSourceTemplate' + template_name, 'runtime.template.concrete')
        classes = getmembers(factory_module,
                            lambda m: isclass(m) and not isabstract(m))

        for name, _class in classes:
            if issubclass(_class, RuntimeSourceTemplate):
                return _class()

