import pytest

from runtime.feed.concrete import RuntimeSourceFeedDocker

from runtime.template.datatype.docker import Image
from runtime.template.datatype.docker import Env
from runtime.template.datatype.docker import Copy
from runtime.template.datatype.docker import Run
from runtime.template.datatype.docker import Cmd

class TestClassRuntimeSourceFeedDocker(object):
    @pytest.fixture
    def instance(request):
        source = {
                "image": {
                    "name": "opensuse",
                    "tag": "42.3"
                },
                "env": {
                    "MONGO_HOST": "localhosot",
                    "MONGO_DB": "27017"
                },
                "copy": {
                    "from": ".",
                    "to": "/workdir"
                },
                "run":["zypper ref", "zypper dup", "zypper in telnet"],
                "cmd": "echo Hello world!\n!"
        }
         
        data = RuntimeSourceFeedDocker()
        data.parse_low(source)
        return data

    def test_to_dict(self, instance):
        source = {
                "image": {
                    "name": "opensuse",
                    "tag": "42.3"
                },
                "env": {
                    "MONGO_HOST": "localhosot",
                    "MONGO_DB": "27017"
                },
                "copy": {
                    "from": ".",
                    "to": "/workdir"
                },
                "run":["zypper ref", "zypper dup", "zypper in telnet"],
                "cmd": "echo Hello world!\n!"
        }
        
        image = Image(source["image"]["name"], source["image"]["tag"])
        env = Env(source["env"])
        copy = Copy(source["copy"]["from"],source["copy"]["to"])
        run = Run(source["run"])
        cmd = Cmd(source["cmd"])

        data = {
                "image": image,
                "env": env,
                "copy": copy,
                "run": run,
                "cmd": cmd
        }

        to_dict = instance.to_dict()

        assert to_dict["image"].name == data["image"].name
        assert to_dict["image"].tag == data["image"].tag

        assert to_dict["env"].export == data["env"].export

        assert to_dict["copy"].dfrom == data["copy"].dfrom
        assert to_dict["copy"].dto == data["copy"].dto

        assert to_dict["run"].commands == data["run"].commands

        assert to_dict["cmd"].command == data["cmd"].command

    def test_parse_low(self,instance):
        source = {
                "image": {
                    "name": "opensuse",
                    "tag": "42.3"
                },
                "env": {
                    "MONGO_HOST": "localhosot",
                    "MONGO_DB": "27017"
                },
                "copy": {
                    "from": ".",
                    "to": "/workdir"
                },
                "run":["zypper ref", "zypper dup", "zypper in telnet"],
                "cmd": "echo Hello world!\n!"
        }
        
        image = Image(source["image"]["name"], source["image"]["tag"])
        env = Env(source["env"])
        copy = Copy(source["copy"]["from"],source["copy"]["to"])
        run = Run(source["run"])
        cmd = Cmd(source["cmd"])

        assert image.name == instance.image.name
        assert image.tag == instance.image.tag

        assert env.export == instance.env.export

        assert copy.dfrom == instance.copy.dfrom
        assert copy.dto == instance.copy.dto

        assert run.commands == instance.run.commands

        assert cmd.command == instance.cmd.command
