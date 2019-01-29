import pytest

from runtime.feed.concrete import RuntimeSourceFeedDocker

from runtime.template.datatype.docker import Image
from runtime.template.datatype.docker import Env
from runtime.template.datatype.docker import Copy
from runtime.template.datatype.docker import Run
from runtime.template.datatype.docker import Cmd

from adapter.concrete import AdapterDocker

class TestClassAdapterDocker(object):
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

        return AdapterDocker(source)

    def test_create(self, instance):
        instance.create()

