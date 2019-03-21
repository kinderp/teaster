from __future__ import print_function
import libvirt
import sys
#url_hypervisor = qemu:///system

class Connection:
    def __init__(self, url_hypervisor):
        self.__url_hypervisor = url_hypervisor
        self.__connection = None
        self.connect()

    @property
    def conn(self):
        return self.__connection

    def connect(self):
        if self.__url_hypervisor:
            self.__connection = libvirt.open(self.__url_hypervisor)
            if self.__connection == None:
                print('Failed to open connection to {}'.format(self.__url_hypervisor), file=sys.stderr)
                exit(1)
        else:
            print('Failed missing URI hypervisor', file=sys.stderr)
