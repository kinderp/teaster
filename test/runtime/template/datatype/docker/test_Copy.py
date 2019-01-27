import pytest

from runtime.template.datatype.docker import Copy

class TestClassCopy(object):
    @pytest.fixture
    def instance(request):
        return Copy('.', '/workdir')

    def test_getdfrom(self, instance):
        assert instance.dfrom == '.'

    def test_setdfrom(self, instance):
        instance.dfrom = '/home/user'
        assert instance.dfrom == '/home/user'


    def test_getdto(self, instance):
        assert instance.dto == '/workdir'

    def test_setdto(self, instance):
        instance.dto = 'new_workdir'
        assert instance.dto == 'new_workdir'


