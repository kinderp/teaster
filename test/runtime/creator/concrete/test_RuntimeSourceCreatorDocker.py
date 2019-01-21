import pytest

from runtime.creator.concrete import RuntimeSourceCreatorDocker

class TestClassRuntimeSourceCreatorDocker(object):
    @pytest.fixture
    def instance(request):        
        return RuntimeSourceCreatorDocker()
    
    def test_one(self,instance):
        assert 1 == 1

   
