from lxml import etree

class Builder:
    def __init__(self):
        self.__root = None

    def set_root(self, name):
        self.__root = etree.Element(name)

    def add_subelement(self, father, name):
        sb = etree.SubElement(father, name)
