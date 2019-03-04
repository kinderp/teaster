# rabbit connection settings
host_rabbit = 'localhost'
vhost = None
queue = 'test'
exchange = 'test'
exchange_type = 'direct'
routing = queue
wait_for_rabbit = False
wait_for_teaster = False

# teaster connection settings
host_teaster = 'localhost'

# build docker settings
import os
root_dir = os.path.dirname(os.path.abspath(__file__)).replace('/settings','')
docker_build_dir = '{}/building'.format(root_dir)

