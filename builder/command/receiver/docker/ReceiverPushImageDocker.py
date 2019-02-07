from io import BytesIO
from docker import APIClient

class ReceiverPushImageDocker:

    def __init__(self, repository, tag=None, daemon='unix:///var/run/docker.sock'):
        self.__repository = repository
        self.__tag = tag
        self.__daemon = daemon
        self.credential={"username":"a.caristia@gmail.com" , "password":"qwertyuiop" }
    
    @property
    def daemon(self):
        return self.__daemon

    @daemon.setter
    def daemon(self, daemon):
        self.__daemon = daemon

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, repository):
        self.__repository = repository

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    def push(self):
        cli = APIClient(base_url=self.__daemon)
        return cli.push(self.__repository, tag = self.__tag, auth_config = self.credential, stream=True, decode=True)
