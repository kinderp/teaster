# Create Rabbitmq user
( sleep 20 ; \
rabbitmqctl add_user celery celery ; \
rabbitmqctl add_vhost celery ; \
rabbitmqctl set_user_tags celery celery ; \
rabbitmqctl set_permissions -p celery celery ".*" ".*" ".*" ; \
echo "*** User celery completed. ***" ; \
echo "*** Log in the WebUI at port 15673 (example: http:/localhost:15673) ***") &

# $@ is used to pass arguments to the rabbitmq-server command.
# For example if you use it like this: docker run -d rabbitmq arg1 arg2,
# it will be as you run in the container rabbitmq-server arg1 arg2
rabbitmq-server $@
