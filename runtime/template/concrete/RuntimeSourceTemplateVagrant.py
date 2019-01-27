from ..factory.RuntimeSourceTemplate import RuntimeSourceTemplate

class RuntimeSourceTemplateVagrant(RuntimeSourceTemplate):
    
    def __init__(self):
        self.__template = """TODO"""

    @property
    def template(self):
        return self.__template

