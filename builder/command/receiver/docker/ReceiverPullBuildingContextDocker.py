from mygit import Git
from settings import root_dir, docker_build_dir


class ReceiverPullBuildingContextDocker:
    def __init__(self, url_repo, destination_dir, branch_name):
        self.__url_repo = url_repo
        self.__destination_dir = destination_dir
        self.__branch_name = branch_name
        self.__git = Git()
            
    def create(self):
        self.__git.clone(self.__url_repo, self.__destination_dir)
        self.__git.pull_branch(self.__destination_dir, self.__branch_name)


