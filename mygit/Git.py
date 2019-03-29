from git import Repo
from git import Actor

import os

from settings import root_dir, docker_build_dir

class Git:

    def check_if_a_branch_exist(self, repo_dir, branch):
        repo = Repo('{}/{}'.format(docker_build_dir, repo_dir))
        info = repo.remotes.origin.fetch()
        for elem in info:
            if elem.name == '{}/{}'.format(repo.remotes.origin.name, branch): return True
            
        return False

    def clone(self, url_repo, destination_dir):
        repo = Repo(root_dir)
        
        if not os.path.exists(docker_build_dir):
            os.makedirs(docker_build_dir)

        git = repo.git
        git.clone(url_repo, '{}/{}'.format(docker_build_dir, destination_dir))


    def add_and_commit(self, repo_dir, filename):
        
        author = Actor("teaster", "teaster@suse.com")
        committer = Actor("teaster", "teasterr@suse.com")

        repo = Repo('{}/{}'.format(docker_build_dir, repo_dir))
        new_file_path = os.path.join(repo.working_tree_dir, filename)
        repo.index.add([new_file_path])
        
        repo.index.commit("added Dockerfile", author=author, committer=committer)


    def push(self, repo_dir):
        repo = Repo('{}/{}'.format(docker_build_dir, repo_dir))
        #origin = repo.create_remote('origin', repo.remotes.origin.url)
        repo.remotes.origin.push()

    def branch(self, repo_dir, branch_name):
        repo = Repo('{}/{}'.format(docker_build_dir, repo_dir))
        git = repo.git
        git.checkout('HEAD', b=branch_name)         # create a new aranch
        git.push('--set-upstream', repo.remotes.origin.name, branch_name)

    def pull_branch(self, repo_dir, branch_name):
        repo = Repo('{}/{}'.format(docker_build_dir, repo_dir))
        git = repo.git
        git.checkout('-b', branch_name, '{}/{}'.format(repo.remotes.origin.name, branch_name))
