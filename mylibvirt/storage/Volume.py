from __future__ import print_function
import sys
import libvirt

# storage_pool_name = default

class Volume:
    def __init__(self, connection, storage_pool_name):
        self.__storage_pool_name = storage_pool_name
        self.__conn = connection
        self.__storage_pool = self.__conn.storagePoolLookupByName(storage_pool_name)
        if self.__storage_pool == None:
            print('Failed to find storage pool {}'.format(storage_pool_name), file=sys.stderr)
            exit(1)

    def list_volumes(self):
        stgvols = self.__storage_pool.listVolumes()
        print('Storage pool: {}'.format(self.__storage_pool_name))
        for stgvol in stgvols :
            print('  Storage vol: '+stgvol)


    def create_volume(self, xml):
        stgvol = self.__storage_pool.createXML(xml, 0)
        if stgvol == None:
            print('Failed to create a  StorageVol objects.', file=sys.stderr)
            exit(1)
        return stgvol

    def remove_volume(sefl, stgvol, logically=False):
        if logically:
            stgvol.delete(0)
        else:
            stgvol.wipe(0)


