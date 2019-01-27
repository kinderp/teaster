import pytest

from runtime.template.datatype.docker import Env

class TestClassEnv(object):
    @pytest.fixture
    def instance(request):
        export_dict = {'SQL_HOST': '192.168.1.11', 'SQL_DB': 'my_db'}
        return Env(export_dict)

    def test_getexport(self, instance):
        assert instance.export == {'SQL_HOST': '192.168.1.11', 'SQL_DB': 'my_db'}

    def test_setexport(self, instance):
        instance.export = {'MONDO_DB':'my_db', 'MONGO_PORT': '1234'}
        assert instance.export == {'MONDO_DB':'my_db', 'MONGO_PORT': '1234'}

