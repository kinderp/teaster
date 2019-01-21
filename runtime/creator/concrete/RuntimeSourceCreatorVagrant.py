from ..factory.RuntimeSourceCreator import RuntimeSourceCreator
from runtime.source.concrete import RuntimeSourceVagrant

class RuntimeSourceCreatorVagrant(RuntimeSourceCreator):

    def __init__(self):
        pass

    def create(self):
        return RuntimeSourceVagrant()
