from ..factory.RuntimeSourceFeed import RuntimeSourceFeed

class RuntimeSourceFeedVagrant(RuntimeSourceFeed):

    def __init__(self):
        pass

    def parse(self, **kwargs):
        print(kwargs)

    def parse_low(self, **kwargs):
        print(kwargs)
