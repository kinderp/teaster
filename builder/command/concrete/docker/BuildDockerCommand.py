from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverBuildImageDocker

class BuildDockerCommand(Command):

    def __init__(self, dockerfile, tag, daemon=None):
        if daemon:
            self.__builder = ReceiverBuildImageDocker(dockerfile, tag, daemon)
        else:
            self.__builder = ReceiverBuildImageDocker(dockerfile, tag)

    def execute(self):
        return self.__builder.build()


