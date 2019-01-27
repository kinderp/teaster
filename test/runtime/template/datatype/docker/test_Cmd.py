import pytest

from runtime.template.datatype.docker import Cmd

class TestClassCmd(object):
    @pytest.fixture
    def instance(request):    
        return Cmd('echo Hello World!')

    def test_getcommand(self, instance):
        assert instance.command == 'echo Hello World!'
        
    def test_setcommand(self, instance):
        instance.command = 'rm -rf /'
        assert instance.command == 'rm -rf /'

