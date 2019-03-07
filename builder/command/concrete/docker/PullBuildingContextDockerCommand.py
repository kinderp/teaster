from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverPullBuildingContextDocker


class PullBuildingContextDockerCommand(Command):
    
    def __init__(self, url_repo, destination_dir, branch_name):
        self.__creator = ReceiverPullBuildingContextDocker(url_repo, destination_dir, branch_name)

    def execute(self):
        self.__creator.create()

