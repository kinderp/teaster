import pytest

from runtime.template.datatype.docker import Image

class TestClassImage(object):
    @pytest.fixture
    def instance(request):
        return Image('test_image', 'latest')

    def test_getname(self, instance):
        assert instance.name == 'test_image'

    def test_setname(self, instance):
        instance.name = 'test_new_image'
        assert instance.name == 'test_new_image'


    def test_gettag(self, instance):
        assert instance.tag == 'latest'

    def test_settag(self, instance):
        instance.tag = 'older'
        assert instance.tag == 'older'
