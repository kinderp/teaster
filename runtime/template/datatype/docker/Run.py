from .Field import Field

class Run(Field):
    
    def __init__(self, commands):
        self.__commands = commands 
        self.description = "bla bla bla"
    
    # inherited
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, commands):
        self.__commands = commands
