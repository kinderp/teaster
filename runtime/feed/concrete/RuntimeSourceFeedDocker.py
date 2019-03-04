from ..factory.RuntimeSourceFeed import RuntimeSourceFeed

from runtime.template.datatype.docker import Image
from runtime.template.datatype.docker import Env
from runtime.template.datatype.docker import Copy
from runtime.template.datatype.docker import Run
from runtime.template.datatype.docker import Cmd
from runtime.template.datatype.docker import Workdir

from settings import docker_build_dir

class RuntimeSourceFeedDocker(RuntimeSourceFeed):

    def __init__(self):
        self.__image = None
        self.__env = None
        self.__copy = None
        self.__run = None
        self.__cmd = None
        self.__workdir = None
        self.__yourtag = None

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, env):
        self.__env = env

    @property
    def copy(self):
        return self.__copy

    @copy.setter
    def copy(self, copy):
        self.__copy = copy

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, run):
        self.__run = run

    @property
    def cmd(self):
        return self.__cmd

    @cmd.setter
    def cmd(self, cmd):
        self.__cmd = cmd

    @property
    def workdir(self):
        return self.__workdir

    @workdir.setter
    def workdir(self, workdir):
        self.__workdir = workdir

    @property
    def yourtag(self):
        return self.__yourtag

    @yourtag.setter    
    def yourtag(self, yourtag):
        self.__yourtag = yourtag

    def parse(self, raw):
        id_ = raw["id"]
        #provenv = raw["provenv"]
        #image_name = raw["image"]["name"]
        #image_tag = raw["image"]["tag"]
        #your_tag = raw["yourtag"]

        # check if a reproducer
        reproducer = False
        repo = None
        command = None
        if "reproducer" in raw:
            repo = raw["reproducer"]["repo"]
            command = raw["reproducer"]["command"]
            reproducer = True
        # Note: the reproducer context is a git repo, during the build phase
        #       that repo will be cloned (using id_ as the new cloned dir) into
        #       the docker_build_dir (see settings/Settings.py)

        workdir = '/workdir'
        source = {}
        source["image"] = raw["image"]
        source["workdir"] = workdir

        if reproducer:
            source["copy"] = {}
            source["copy"]["from"] = "{}/{}".format(docker_build_dir, id_)
            source["copy"]["to"] = workdir

            source["cmd"] = command

        source["run"] = raw["provenv"]
        source["yourtag"] = raw["yourtag"]
        source["env"] = {}
        #        source = {
        #            "image": {
        #            "name": image_name,
        #            "tag": image_tag
        #        },
        #        "env": {
        #
        #        },
        #        "workdir":"/workdir",
        #        "copy": {
        #            "from": "{}/{}".format(docker_build_dir, id_),
        #            "to": "/workdir"
        #        },
        #        "run":provenv,
        #        "cmd": "echo Hello world!",
        #        "yourtag": your_tag
        #        }


        self.parse_low(source)

    def parse_low(self, raw):
        self.image = Image(raw["image"]["name"], raw["image"]["tag"])
        self.env = Env(raw["env"])
        self.copy = Copy(raw["copy"]["from"],raw["copy"]["to"])
        self.run = Run(raw["run"])
        self.cmd = Cmd(raw["cmd"])
        self.workdir = Workdir(raw["workdir"])
        self.yourtag = raw["yourtag"]

    def to_dict(self):
        return {
            "image": self.__image,
            "env": self.__env,
            "copy": self.__copy,
            "run": self.__run,
            "cmd": self.__cmd,
            "workdir": self.__workdir,
            "yourtag": self.__yourtag
        }
