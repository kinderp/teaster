from io import BytesIO
from docker import APIClient

class ReceiverBuildImageDocker:

    def __init__(self, dockerfile, tag, daemon='unix:///var/run/docker.sock'):
        self.__dockerfile = dockerfile
        self.__tag = tag
        self.__daemon = daemon

    @property
    def dockerfile(self):
        return self.__dockerfile

    @dockerfile.setter
    def dockerfile(self, dockerfile):
        self.__dockerfile = dockerfile

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def daemon(self):
        return self.__daemon

    @daemon.setter
    def daemon(self, daemon):
        self.daemon = daemon

    def build(self):
        f = BytesIO(self.dockerfile.encode('utf-8'))
        cli = APIClient(base_url=self.__daemon)

        return cli.build(fileobj=f, rm=True, tag=self.__tag)
