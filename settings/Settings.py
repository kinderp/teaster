import os
# rabbit connection settings
host_rabbit = os.environ.get('RABBIT_HOST','localhost')
vhost = None
queue = 'test'
exchange = 'test'
exchange_type = 'direct'
routing = queue
wait_for_rabbit = False
wait_for_teaster = False

# teaster connection settings
host_teaster = os.environ.get('TEASTER_HOST', 'localhost')

# icerlery connection settings
host_icelery = os.environ.get('ICELERY_HOST', 'localhost')
host_rabbit_celery = os.environ.get('RABBIT_CELERY_HOST', 'localhost')

# build docker settings
import os
root_dir = os.path.dirname(os.path.abspath(__file__)).replace('/settings','')
docker_build_dir = '{}/building'.format(root_dir)

