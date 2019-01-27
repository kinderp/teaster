from .Field import Field

class Cmd(Field):
    def __init__(self, command):
        self.__command = command
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
    def command(self):
        return self.__command

    @command.setter
    def command(self, command):
        self.__command = command

