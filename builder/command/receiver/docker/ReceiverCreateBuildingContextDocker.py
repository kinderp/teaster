from mygit import Git
from settings import root_dir, docker_build_dir


class ReceiverCreateBuildingContextDocker:
    def __init__(self, url_repo, destination_dir, dockerfile, branch_name):
        self.__dockerfile = dockerfile
        self.__url_repo = url_repo
        self.__destination_dir = destination_dir
        self.__branch_name = branch_name
        self.__git = Git()
            
    def create(self):
        # clone repo into dest dir
        self.__git.clone(self.__url_repo, self.__destination_dir)
        import pdb
        pdb.set_trace()
        self.__create_new_branch()
        self.__write_dockerfile()
        self.__push_dockerfile()

    def __create_new_branch(self):
        if self.__git.check_if_a_branch_exist(self.__destination_dir, self.__branch_name):
            self.__git.pull_branch(self.__destination_dir, self.__branch_name)
        else:
            self.__git.branch(self.__destination_dir, self.__branch_name)

    def __write_dockerfile(self):
        with open('{}/{}/Dockerfile'.format(docker_build_dir, self.__destination_dir), 'w') as myfile:
            myfile.write(self.__dockerfile)


    def __push_dockerfile(self):
        self.__git.add_and_commit(self.__destination_dir, 'Dockerfile')
        self.__git.push(self.__destination_dir)

