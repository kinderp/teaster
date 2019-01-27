from ..factory.RuntimeSourceCreator import RuntimeSourceCreator
from runtime.source.concrete import RuntimeSourceVagrant

class RuntimeSourceCreatorVagrant(RuntimeSourceCreator):

    def __init__(self):
        pass

    def create(self, source_feed, source_template):
        # insert here logic to create RuntimeSourceVagrant
        # from RuntimeSourceFeedVagrant RuntimeSourceTemplateVagrant
        return RuntimeSourceVagrant()
