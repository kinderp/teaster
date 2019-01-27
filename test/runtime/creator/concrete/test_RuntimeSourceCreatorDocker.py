import pytest

from runtime.creator.concrete import RuntimeSourceCreatorDocker
from runtime.feed.concrete import RuntimeSourceFeedDocker
from runtime.template.concrete import RuntimeSourceTemplateDocker

class TestClassRuntimeSourceCreatorDocker(object):
    @pytest.fixture
    def instance(request):        
        return RuntimeSourceCreatorDocker()
    
    def test_create(self,instance):
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
         
        source_feed = RuntimeSourceFeedDocker()
        source_feed.parse_low(source)

        source_template = RuntimeSourceTemplateDocker()

        source_runtime = instance.create(source_feed, source_template)

        print(source_runtime.show())

   
