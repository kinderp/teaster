from .Field import Field

class Copy(Field):
    def __init__(self, from_, to_):
        self.__from = from_
        self.__to = to_
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
    def dfrom(self):
        return self.__from

    @dfrom.setter
    def dfrom(self, from_):
        self.__from = from_


    @property
    def dto(self):
        return self.__to

    @dto.setter
    def dto(self, to_):
        self.__to = to_
