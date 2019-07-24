from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverDestroyBuildingContextDocker

class DestroyBuildingContextDockerCommand(Command):

    def __init__(self, destination_dir):
        self.__creator = ReceiverDestroyBuildingContextDocker(destination_dir)

    def execute(self):
        self.__creator.create()
