from __future__ import print_function
import sys
import libvirt

xmlconfig = '<domain>........</domain>'

class Installer:
    def __init__(self, connection):
        #self.__conn = self.__connect()
        
        self.__conn = connection

#    def __connect(self):
#        conn = libvirt.open('qemu:///system')
#        if conn == None:
#            print('Failed to open connection to qemu:///system', file=sys.stderr)
#            exit(1)
#        return conn


    def install(self, xml):
        dom = self.__conn.createXML(xml, 0)
        if dom == None:
            print('Failed to create a domain from an XML definition.', file=sys.stderr)
            exit(1)

        print('Guest '+dom.name()+' has booted', file=sys.stderr)
        self.__conn.close()
