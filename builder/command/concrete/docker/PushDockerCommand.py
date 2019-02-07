from builder.command.abstract import Command
from builder.command.receiver.docker import ReceiverPushImageDocker

class PushDockerCommand(Command):

    def __init__(self, repository, tag=None):
        self.__pusher = ReceiverPushImageDocker(repository, tag)
       
    def execute(self):
        return self.__pusher.push()


