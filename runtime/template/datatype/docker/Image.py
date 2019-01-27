from .Field import Field

class Image(Field):
    def __init__(self, name, tag):
        self.description = "bla bla bla"
        self.__name = name
        self.__tag = tag
    
    # inherited
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # own
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

