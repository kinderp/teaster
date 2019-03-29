from flask import Flask, request
from celery import Celery
import json

from builder.command.concrete.docker import CreateBuildingContextDockerCommand
from builder.command.concrete.docker import BuildFromDirDockerCommand
from builder.command.concrete.docker import PushDockerCommand

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'pyamqp://celery:celery@localhost:5672/celery'
#app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)



@celery.task
def build_docker(data):
    
    #    repo = 'https://github.com/kinderp/testproject.git'
    #    destination_dir = '1232456abc'
    #    docker_file = data

    repo = data["repo"]
    destination_dir = data["target_dir"]
    docker_file = data["runtime_source"]
    working_branch = data["working_branch"]

    print(repo)
    print(destination_dir)
    print(working_branch)
    # What does CreateBuildingContextDockerCommand do ?
    #
    # 1. clone repo in reproducer.repo field
    # 2. create a new branch with the same name in image.name field
    # 3. create a Dockerfile in that branch
    # 4. push all

    print("=={}==".format("Cloning..."))
    b = CreateBuildingContextDockerCommand(repo, destination_dir, docker_file, working_branch)
    b.execute()


    print("=={}==".format("Building..."))
    # it just build an image from a Dockerfile previous created
    builder = BuildFromDirDockerCommand('building/{}'.format(destination_dir), 'registry.gitlab.com/caristia/antonio_suse/new_image')
    #response = [line for line in builder.execute()]
    #print(response)
    for line in builder.execute():
        print(line)

    # it just push to a docker registry
    print("=={}==".format("Pushing..."))
    pusher = PushDockerCommand('registry.gitlab.com/caristia/antonio_suse/new_image')
    #p_response = [line for line in pusher.execute()]
    #print(p_response)
    for line in pusher.execute():
        print(line)



@app.route('/build_docker', methods=['POST'])
def building_docker():
    import pdb
    pdb.set_trace()
    data = request.data


    task = build_docker.delay(json.loads(request.data))
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)

