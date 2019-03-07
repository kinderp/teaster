from io import BytesIO
from docker import APIClient

class ReceiverBuildFromDirImageDocker:

    def __init__(self, build_dir, tag, daemon='unix:///var/run/docker.sock'):
        self.__build_dir = build_dir
        self.__tag = tag
        self.__daemon = daemon

    @property
    def build_dir(self):
        return self.__build_dir

    @build_dir.setter
    def dockerfile(self, build_dir):
        self.__build_dir = build_dir

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
        cli = APIClient(base_url=self.__daemon)

        return cli.build(path=self.__build_dir, rm=True, tag=self.__tag)
