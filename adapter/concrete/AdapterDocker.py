from ..factory.Adapter import Adapter
#from runtime.feed.concrete import RuntimeSourceFeedDocker
#from runtime.template.concrete import RuntimeSourceTemplateDocker

class AdapterDocker(Adapter):

    def create(self):

        # use self.tloader to create the concrete RuntimeSourceTemplateFactory

        # use self.floader to create the concrete RuntimeSourceFeed factory
        # pass self.adaptee (dict obj from flask request) to create method and get a RuntimeSourceFeedDocker obj

        # use self.cloader to create the concrete RuntimeSourceCreator factory
        # pass

        docker_template = self.tloader.load_template('Docker')

        docker_feed = self.floader.load_feed('Docker')
        docker_feed.parse_low(self.adaptee)

        docker_creator = self.cloader.load_factory('Docker')
        docker_source = docker_creator.create(docker_feed, docker_template)
        print(docker_source.show())
        return docker_source.source
