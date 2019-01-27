import pytest

from runtime.template.datatype.docker import Run

class TestClassRun(object):
    @pytest.fixture
    def instance(request):
        commands = ['apt-get update','apt-get install -y --no-install-reccomends gcc python-dev','rm -rf /var/lib/apt/lists/*', 'apt-get purge -y --autpremove gcc python-dev']
        return Run(commands)

    def test_getcommands(self, instance):
        assert instance.commands == ['apt-get update','apt-get install -y --no-install-reccomends gcc python-dev','rm -rf /var/lib/apt/lists/*', 'apt-get purge -y --autpremove gcc python-dev']

    def test_setcommands(self, instance):
        instance.commands = ['one_command','another_command']
        assert instance.commands == ['one_command','another_command']

