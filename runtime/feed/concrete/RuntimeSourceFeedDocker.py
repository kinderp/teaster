from ..factory.RuntimeSourceFeed import RuntimeSourceFeed

from runtime.template.datatype.docker import Image
from runtime.template.datatype.docker import Env
from runtime.template.datatype.docker import Copy
from runtime.template.datatype.docker import Run
from runtime.template.datatype.docker import Cmd

class RuntimeSourceFeedDocker(RuntimeSourceFeed):

    def __init__(self):
        self.__image = None
        self.__env = None
        self.__copy = None
        self.__run = None
        self.__cmd = None

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

    def parse(self, raw):
        print(kwargs)

    def parse_low(self, raw):
        self.image = Image(raw["image"]["name"], raw["image"]["tag"])
        self.env = Env(raw["env"])
        self.copy = Copy(raw["copy"]["from"],raw["copy"]["to"])
        self.run = Run(raw["run"])
        self.cmd = Cmd(raw["cmd"])
        
    def to_dict(self):
        return {
            "image": self.__image,
            "env": self.__env,
            "copy": self.__copy,
            "run": self.__run,
            "cmd": self.__cmd
        }
