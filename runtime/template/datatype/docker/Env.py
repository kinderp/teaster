from .Field import Field

class Env(Field):
    
    def __init__(self, export):
        self.description = "bla bla bla"
        self.__export = export

    # inherited
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # own
    @property
    def export(self):
        return self.__export

    @export.setter
    def export(self, export):
        self.__export = export
