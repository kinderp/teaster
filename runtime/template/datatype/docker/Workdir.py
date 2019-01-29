from .Field import Field

class Workdir(Field):
    def __init__(self, workdir):
        self.__workdir = workdir
        self.description = "bla bla bla"
    
    # inherited
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # own
    @property
    def workdir(self):
        return self.__workdir

    @workdir.setter
    def workdir(self, workdir):
        self.__workdir = workdir

