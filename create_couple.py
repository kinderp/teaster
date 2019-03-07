from adapter.concrete import AdapterDockerHLA
from builder.command.concrete.docker import BuildDockerCommand
from builder.command.concrete.docker import BuildFromDirDockerCommand
from builder.command.concrete.docker import PushDockerCommand

from builder.command.concrete.docker import CreateBuildingContextDockerCommand
from builder.command.concrete.docker import PullBuildingContextDockerCommand
# this is what arrive from queue

source = {
    "id": "1234abc",
    "provenv": ["zypper --non-interactive in telnet","zypper --non-interactive in vim"],
    "yourtag": "registry.gitlab.com/caristia/antonio_suse/new_image",
    "reproducer": {
        "repo": "https://github.com/kinderp/testproject.git",
    }
}

# a consumer will add an image name and a tag

source["image"] = {}
source["image"]["name"] = "opensuse"
source["image"]["tag"] = "42.3"

a = AdapterDockerHLA(source)

docker_file = a.create()

print(docker_file)

repo = source["reproducer"]["repo"]
destination_dir = source["id"]

import pdb
pdb.set_trace()

# What does CreateBuildingContextDockerCommand do ?
#
# 1. clone repo in reproducer.repo field
# 2. create a new branch with the same name in image.name field
# 3. create a Dockerfile in that branch
# 4. push all 

b = CreateBuildingContextDockerCommand(repo, destination_dir, docker_file, source['image']['name'])
b.execute()

# rm the building env

import shutil
shutil.rmtree('building/{}'.format(destination_dir))

# What does PullBuildingContextDockerCommand do ?
#
# 1. clone repo in reproducer.repo field
# 2. pull the building branch created in the previous step 

c = PullBuildingContextDockerCommand(repo, destination_dir, source['image']['name'])
c.execute()

# it just build an image from a Dockerfile previous created
builder = BuildFromDirDockerCommand('building/{}'.format(destination_dir), 'registry.gitlab.com/caristia/antonio_suse/new_image')
response = [line for line in builder.execute()]
print(response)


#registry.gitlab.com/caristia/antonio_suse/optional-image-name:tag
#builder = BuildDockerCommand(docker_file, 'registry.gitlab.com/caristia/antonio_suse/new_image')
#response = [line for line in builder.execute()]
#print(response)

# it just push to a docker registry
pusher = PushDockerCommand('registry.gitlab.com/caristia/antonio_suse/new_image')
p_response = [line for line in pusher.execute()]
print(p_response)
