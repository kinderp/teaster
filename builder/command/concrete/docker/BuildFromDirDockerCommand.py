from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverBuildFromDirImageDocker

class BuildFromDirDockerCommand(Command):

    def __init__(self, build_dir, tag, daemon=None):
        if daemon:
            self.__builder = ReceiverBuildFromDirImageDocker(build_dir, tag, daemon)
        else:
            self.__builder = ReceiverBuildFromDirImageDocker(build_dir, tag)

    def execute(self):
        return self.__builder.build()


