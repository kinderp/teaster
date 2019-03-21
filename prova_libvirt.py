image_name = 'test.qcow2'

iso_path = '/home/antonio/SLE-15-Installer-DVD-x86_64-GM-DVD1.iso'

xml = """
<domain type='kvm'>
  <name>demo</name>
  <uuid>c7a5fdbd-cdaf-9455-926a-d65c16db1809</uuid>
  <memory unit='KiB'>2097152</memory>
  <vcpu>1</vcpu>
  <os>
    <type arch='x86_64' machine='pc'>hvm</type>
    <boot dev='hd'/>
    <boot dev='cdrom'/>
  </os>  
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <emulator>/usr/bin/qemu-kvm</emulator>
    <disk type='file' device='disk'>
      <source file='/var/lib/libvirt/images/{image_name}'/>
      <driver name='qemu' type='qcow2'/>
      <target dev='hda'/>
    </disk>
    <disk type='file' device='cdrom'>
        <source file='{iso_path}'/>
        <target dev='hdc' bus='ide'/>
    </disk>
    <interface type='network'>
      <mac address='52:54:00:94:f0:a4'/>
      <source network='default'/>
      <model type='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </interface>
    <input type='mouse' bus='ps2'/>
    <graphics type='vnc' port='8888' listen='127.0.0.1'/>
  </devices>
</domain>

""".format(image_name=image_name, iso_path=iso_path)

from mylibvirt.connection import Connection
from mylibvirt.installer import Installer
from mylibvirt.storage import Volume

url_hypervisor = 'qemu:///system'
c = Connection(url_hypervisor)

stgvol_xml = """
<volume>
  <name>{image_name}</name>
  <allocation>0</allocation>
  <capacity unit="G">10</capacity>
  <target>
    <format type='qcow2'/>
    <path>/var/lib/virt/images/{image_name}</path>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>""".format(image_name=image_name)

v = Volume(c.conn, 'default')
v.list_volumes()

#new_volume = v.create_volume(stgvol_xml)

import pdb
pdb.set_trace()
i = Installer(c.conn)
i.install(xml)
