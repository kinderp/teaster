from ..factory.RuntimeSource import RuntimeSource

class RuntimeSourceDocker(RuntimeSource):
   
    def __init__(self, source):
        self.__source = source

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source == source

    def show(self):
        print(self.__source)

