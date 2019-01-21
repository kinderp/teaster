from ..factory.RuntimeSourceCreator import RuntimeSourceCreator
from runtime.source.concrete import RuntimeSourceDocker


class RuntimeSourceCreatorDocker(RuntimeSourceCreator):

    def __init__(self):
        pass

    def create(self):
        return RuntimeSourceDocker()
