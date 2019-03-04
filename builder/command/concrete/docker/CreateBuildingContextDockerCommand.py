from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverCreateBuildingContextDocker


class CreateBuildingContextDockerCommand(Command):
    
    def __init__(self, url_repo, destination_dir, dockerfile, branch_name):
        self.__creator = ReceiverCreateBuildingContextDocker(url_repo, destination_dir, dockerfile, branch_name)

    def execute(self):
        self.__creator.create()

