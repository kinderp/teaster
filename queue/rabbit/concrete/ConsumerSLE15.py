from ..concrete.Consumer import Consumer
from ..Settings import no_ack

#from adapter.concrete import AdapterDocker
#from builder.command.concrete.docker import BuildDockerCommand
#from builder.command.concrete.docker import PushDockerCommand
#
#source = {
#    "image": {
#    "name": "opensuse",
#    "tag": "42.3"
#},
#"env": {
#    "MONGO_HOST": "localhosot",
#    "MONGO_DB": "27017"
#},
#"workdir":".",
#"copy": {
#    "from": ".",
#    "to": "/workdir"
#},
#"run":["zypper --non-interactive ref", "zypper --non-interactive dup", "zypper --non-interactive in telnet"],
#"cmd": "echo Hello world!"
#}
#
#a = AdapterDocker(source)
#docker_file = a.create()
##registry.gitlab.com/caristia/antonio_suse/optional-image-name:tag
#builder = BuildDockerCommand(docker_file, 'registry.gitlab.com/caristia/antonio_suse/new_image')
#response = [line for line in builder.execute()]
#print(response)
#
#pusher = PushDockerCommand('registry.gitlab.com/caristia/antonio_suse/new_image')
#p_response = [line for line in pusher.execute()]
#



class ConsumerSLE15(Consumer):
  
    def callback(self, channel, method, properties, body):
        print("[ConsumerSLE15] Received %r" % body)
        # TODO put here all the code to create json data for AdapterDocker
        self.ack(delivery_tag=method.delivery_tag)

