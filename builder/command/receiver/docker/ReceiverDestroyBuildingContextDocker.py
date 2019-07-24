from shutil import rmtree

from settings import docker_build_dir

class ReceiverDestroyBuildingContextDocker:
    def __init__(self, destination_dir):
        self.__destination_dir = destination_dir

    def create(self):
        rmtree('{}/{}'.format(docker_build_dir, self.__destination_dir))
