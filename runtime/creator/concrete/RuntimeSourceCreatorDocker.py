from ..factory.RuntimeSourceCreator import RuntimeSourceCreator
from runtime.source.concrete import RuntimeSourceDocker

from jinja2 import Template

class RuntimeSourceCreatorDocker(RuntimeSourceCreator):

    def __init__(self):
        pass

    def create(self, source_feed, source_template):
        # insert here logic to create RuntimeSourceDocker
        # from RuntimeSourceFeedDocker RuntimeSourceTemplateDocker
        template = Template(source_template.template)
        runtime_source_raw = template.render(source_feed.to_dict())
        return RuntimeSourceDocker(runtime_source_raw)
