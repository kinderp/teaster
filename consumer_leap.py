from queue.rabbit.concrete import Consumer
import json
import requests

from settings import host_rabbit, vhost, queue, exchange, exchange_type, routing, wait_for_rabbit, wait_for_teaster

from adapter.concrete import AdapterDockerHLA
from builder.command.concrete.docker import CreateBuildingContextDockerCommand

# docker-compose doesn't garantee anything about services startup order
# so wait until rabbirmq connection is available


result = Consumer.register('docker','leap:42.3', wait_for_teaster)

print("registration result \n{}".format(json.dumps(result, indent=4, sort_keys=True)))

queue = result['id']
routing = queue

#print("queue: {}".format(queue))

def my_callback(body):
    """
        source = {
        "id": "1234abc",
        "provenv": ["zypper --non-interactive in telnet","zypper --non-interactive in vim"],
        "yourtag": "registry.gitlab.com/caristia/antonio_suse/new_image",
        "reproducer": {
            "repo": "https://github.com/kinderp/testproject.git",
        }
    }
    """
    source = json.loads(body)
    source["image"] = {}
    source["image"]["name"] = "opensuse"
    source["image"]["tag"] = "42.3"

    a = AdapterDockerHLA(source)

    docker_file = a.create()
    payload = {
        "runtime_source": docker_file,
        "repo": source["reproducer"]["repo"],
        "target_dir": "1232456abc",
        "working_branch": source["image"]["name"]
    }

    r = requests.post("http://localhost:6000/build_docker", json=payload)

conn_details = {
        "host" :host_rabbit, 
        "vhost" : vhost,
        "queue" : queue, 
        "exchange" : exchange, 
        "exchange_type" : exchange_type, 
        "routing" : routing,
        "wait_for_rabbit": wait_for_rabbit
}

print("producer, connecting to rabbit: \n{}".format(json.dumps(conn_details,indent=4, sort_keys=True)))

p = Consumer(**conn_details)

p.consume(my_callback)

