# teaster

Teaster: automate your dirty tester work and take time for a relaxing tea.

![alt text](https://github.com/kinderp/teaster/blob/master/diagram1.png)

# Manual Installation

A complete docker compose dev env is not ready yet, sorry. 

But you can install all the necessary parts manually :)

Please, follow the below instructions

### Install rabbitmq

`sudo zypper in rabbitmq-server rabbitmq-server-plugins`

`sudo systemctl start rabbitmq-server`

`sudo rabbitmq-plugins enable rabbitmq_management`

### Set conf for celery tasks

`sudo rabbitmqctl add_user celery celery`

`sudo rabbitmqctl add_vhost celery`

`sudo rabbitmqctl set_user_tags celery celery`

`sudo rabbitmqctl set_permissions -p celery celery ".*" ".*" ".*"`

### Setup a dev env

[click here](https://github.com/kinderp/teaster/blob/master/README.md#set-up-dev-environment)

### Activate your dev env and install all the deps

`antonio@linux-h1g7:~/dev/teaster> workon teaster`

`(teaster) antonio@linux-h1g7:~/dev/teaster> sudo pip install -r requirements.txt`
 

# Run and test the system

:warning: teaster is just a POC and it is in the early stage of his hard life. Does not exist any validation for the input requests yet and unit tests cover just a little part of the entire codebase. So what teaster does well untill now is: it crashes :boom: and make you feel frustated :)

### Run input interface

```
(teaster) ➜  teaster git:(master) ✗ python main.py 
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 208-391-154
```

### Run a consumer


Before running a consumer, be sure to have rabbitmq-server up and running


`sudo systemctl status rabbitmq-server`


then run your consumer


```
(teaster) ➜  teaster git:(master) ✗ python consumer_leap.py 
 [Consumer] registering a consumer to teaster localhost
 [Consumer] response registration 
{
    "id": "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b", 
    "product": "leap:42.3", 
    "runenv": "docker"
}

registration result 
{
    "id": "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b", 
    "product": "leap:42.3", 
    "runenv": "docker"
}
consumer, connecting to rabbit: 
{
    "exchange": "test", 
    "exchange_type": "direct", 
    "host": "localhost", 
    "queue": "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b", 
    "routing": "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b", 
    "vhost": null, 
    "wait_for_rabbit": false
}
 [*] Waiting for messages. To exit press CTRL+C

```

As you can see below, what a consumer does:

1. it registers itself to the system

     During this phase an id is generated by the system for the consumer.
     You can use this id to send requests to that specific consumer.
     A queue named with that id is created on rabbitmq.

2. It connects to the new created queue (see id before)

3. It waits for a new message 

You can verify that a consumer now exists from:

1. rabbitmq side

```
(teaster) ➜  teaster git:(master) ✗ sudo rabbitmqctl list_consumers -p /
Listing consumers
6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b	<rabbit@linux-peu5.2.540.0>	ctag1.5ad98e68d87a4dbf877b51d89b3dbb5a	true	0	[]
```

2. teaster side

```
(teaster) ➜  teaster git:(master) ✗ curl http://localhost:5000/consumers
{
    "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b": {
        "id": "6dd47d81e014ad9de81161951814bf50e4e1246bb7a43404ffb84ab31ef7d18b", 
        "product": "leap:42.3", 
        "runenv": "docker"
    }
}
```

### Run celery input interface

It accepts building request for your celery tasks

```
(teaster) ➜  teaster git:(master) ✗ python icelery.py
 * Serving Flask app "icelery" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:6000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 208-391-154
```

### Run your celery workers

```
(teaster) ➜  teaster git:(master) ✗ celery worker -A icelery.celery --loglevel=info
 
 -------------- celery@linux-peu5 v4.2.2 (windowlicker)
---- **** ----- 
--- * ***  * -- Linux-4.12.14-lp150.12.16-default-x86_64-with-glibc2.2.5 2019-03-31 12:50:41
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         icelery:0x7fbf0ac45250
- ** ---------- .> transport:   amqp://celery:**@localhost:5672/celery
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . icelery.build_docker

[2019-03-31 12:50:42,123: INFO/MainProcess] Connected to amqp://celery:**@127.0.0.1:5672/celery
[2019-03-31 12:50:42,408: INFO/MainProcess] mingle: searching for neighbors
[2019-03-31 12:50:43,705: INFO/MainProcess] mingle: all alone
[2019-03-31 12:50:43,757: INFO/MainProcess] celery@linux-peu5 ready.
```

# Introduction

Here just some definitions to speak the same language.

As a tester your work can be summarized in these steps:

1. Get instructions from bugzilla page and try to build a reprodcer.
   
   A reproducer can be:
   
    * a cli reproducer (a bash script or an openqa testmodule) 
    * a gui reproducer (an openqa testmodule + needles)
   
   Any reproducer needs a runtime environment to be executed.
   
   A runtime environment can be:
   
    * a container
    * a virtual machine
    
   A runtime environment + reproducer can be packed in a automation environments.
   
   An automation environment contains:
   
    - a runtime environment
    - all the provisioned software (before or after).
      to be consistent we'll name that provisioning environment
    - a reproducer
   
   An automation environment can be represented by a tuple:
   
   `(runtime env, provisioning env, reproducer)`
   
   All the possible combinations of these three components create an automation environment:
   
   Cli automation environments
    * (container, packages before update, script bash)
    * (container, packages after update, script bash)
    * (container + openqa instance, packages before update, openqa testmodule)
    * (cotaniner + openqa instance, packages after  update, openqa testmodule)
    * (vm, packages before update, script bash)
    * (vm, packages after  update, script bash)
    * (vm + openqa instance, packages before update, openqa testmodule)
    * (vm + openqa instance, packages after  update, openqa testmodule)

   Gui automation environments
    * (container + openqa instance, packages before update, openqa testmodule + needles)
    * (cotaniner + openqa instance, packages after  update, openqa testmodule + needles)
    * (vm + openqam instance, packages before update, openqa testmodule + needles)
    * (vm + openqa instance, packages after  update, openqa testmodule + needles)
    
2. Provisioning of the runtime environment (and installation tests)

    We need to be sure that the packages we are testing can be installed on top of our runtime environment.
    We are helped on that by tools like mtui but sometimes it needs some manual work and anyway it's not a completely automated process.
    
3. Reproducing 

   Reproduce the bug before and after (update and downgrade)
   Even during this phase mtui is our friend.
   
4. Comparison

In this scenario just only the first phase (the mental process to figure out the better reproducer)
really requires an human intellectual intervention.

The same reproducer is applied (manually) to different products. So all the steps of the entire process
are repeated by testers with a lof of wasting time.

As a tester before going through all the entire process i want:

Know if a tester has already worked on that bug, in other words if a reproducer for that particul bug already exists for other products. (We do that manually searching for a bug in qam.suse)

  if it's the first time that bug is tested (no reproducer for that bug)
  
   (a)
   1. Concentrate just only on the reproducer
   2. Get automagically a runtime env + a provisioning env (e.g. a container with all provisioned packages)
   3. Once finished creating the reproducer, pack all (run env, prov env, reproducer) and push that one somewheree and share with all other testers in the future. In other words we're creating the tuple, the automation environment.
    
  if a reproducer already exists:
   
   (b)
   1. Get automagically an automation environment with the testing package installed (provisioning) and the reproducer ready to be executed
   2. Chose the runtime environment i like (container or vm)
   3. Run the reproducer  (before and after)
   4. Compare the results (before and after)

In the first case (a) we build an automation environment joining our reproducer,the packages and the runtime environment.
In the second one (b) we use an automation envinronment to test our bugs.

# Use Cases

- **Autoregister** (uc#0)
 
    _Actors_:

         - A consumer: it wants to inform the system about its presence and capabilities. 
                       A consumer is able to handle only a runtime env and only a product

    _Input_: 

         - (run env, product) e.g. (docker, sle12sp3)

    _Output_: 

         - a consumer id. 
           The system assigns an id to the consumer. 

    _Description_:

         - Before starting its lifecycle the consumer needs to inform the system 
           about which particular run env and product it is able to handle

- **Search for a consumer** (uc#1)
 
     _Actors_:

         - Started by guy: He wants to know if does exist a consumer able to handle (run env, product) 
                           for a prov env.
         - Tester        : same above.
 
         A consumer can handle only one run env and only one product.
         A prov env are the packages to test.

    _Input_: 

         - (run env, product) e.g. (docker, sle12sp3)

    _Output_: 

         - a consumer id or an error. 

    _Description_:

         -  Search for a consumer that is able to create a couple for a particular product
            and a particular run env.
         -  The system responds with a consumer id in case of success or some sort of error.

- **Search for a reproducer** (uc#2)
 
     _Actors_:

         - Started by guy: He wants to know if already exist a reprodcuer for a bug.
         - Tester        : same above.

    _Input_: 

         - (bug_id, reproducer_type) 

    _Output_: 

         - (reproducer_id, link to the reproducer)
         
         link to a bash script
         link to a testmodule
         link to testmodule and needles

    _Description_:

         -  Search for a reproducer
         -  The system responds with a reproducer id and a link to view the reproducer or an error.
         -  The reproduer id will be used to forward the triple creation request 
            (run env, prov env, reproducer) to the correct consumer. 
            See above uc#1 to search for the correct consumer for a run env and a product 

- **Create a triple** (uc#3)

     In this case the reproducer already exists. We got an id from #uc2.
     
     _Actors_:

         - Started by guy: He wants to create the triple 
                           (run env, prov env, reproducer) for a new update in the queue.
         - Tester        : He wants to create the couple 
                           (run env, prov env, reproducer) to investigate about something.
         - A consumer    : It knows how to handle that particular run env and product. 
                           It contacts the builder.
         - A builder     : It creates the triple: an automation env

         The first 2 actors must know:
         1. the consumer id   (from uc#1)
         2. the reproducer id (from uc#2)

    _Input_: 

         - (consumer id, reproducer id, prov env) e.g. (1234, xxxxx, [a.x.y.z])

    _Output_: 

         - An url poiting to (run env, prov env, reproducer). 
         
            A registry url:
            hashicorp/precise64
            opensuse/tumbleweed 

    _Description_:

         -  The first 2 actors submit the request to the consumer, using the correct id.
            The consumer creates or modifies the source (Dockerfile, Vagranfile) for 
            provisioning of the testing packages and reproducer. 
            Then the consumer forwards the modified source to the builder (destionation).
            The builder builds (run env, prov env, reproducer) 
            
      (Note) the building process will be an asynchronous process so we need some sort of notification.



- **Create a couple** (uc#4)

    In this case the reproducer does not exist. We got an error from #uc2.
    
     _Actors_:

         - Started by guy: He wants to create the couple 
                           (run env, prov env) for a new update in the queue.
         - Tester        : He wants to create the couple 
                           (run env, prov env) to investigate about something.
         - A consumer    : It knows how to handle that particular run env and product. 
                           It contacts the builder.
         - A builder     : It creates the run env.

         The first 2 actors must know:
         1. the consumer id (from uc#1) 

    _Input_: 

         - (consumer id, prov env) e.g. (1234, [a.x.y.z])

    _Output_: 

         - An url poiting to (run env, prov env). 
         
            A registry url:
            hashicorp/precise64
            opensuse/tumbleweed 

    _Description_:

         -  The first 2 actors submit the request to the consumer, using the correct id.
            The consumer creates or modifies the source (Dockerfile, Vagranfile) 
            for provisioning of testing packages. 
            Then the consumer forwards the modified source to the builder (destionation).
            The builder builds (run env, prov env) 
            
      (Note) the building process will be an asynchronous process so we need some sort of notification.


- **Share a reproducer** (uc#5)

 
     _Actors_:

         - Tester        : He wants to share a reproducer for a particular bug.

    _Input_: 

         - (bug id, reproducer) 

    _Output_: 

         - (link to the reproducer) or an error
         
         link to a bash script
         link to a testmodule
         link to testmodule and needles
         
    _Description_:

         -  The tester sends the reproducer.
            The system saves the reproducer somewhere and returns a link.

# Class analysis

Some notes about classes and patterns

## Class analysis for run time source creation

1. We'll use a [Factory Method](https://en.wikipedia.org/wiki/Factory_method_pattern) to instance the concrete RuntimeSource
2. We'll use a [Adapter](https://en.wikipedia.org/wiki/Adapter_pattern) to create a RuntimeeSourceFeed concrete object from json data requests. In this way, we put all the creation logic into the adapter and we are free to change the internal interface holding the external one (flask reuqest) always the same.

------------------------

      RuntimeSourceFeed: 

            it represents all the infos needed to feed Dockerfile or Vagrantfile templates.
            it is an abstract class and defines the interface for all the concrete RuntimeSourceFeed objects
            RuntimeSourceFeedDocker,RuntimeSourceFeedVagrant

      RuntimeSourceFeedDocker: it is a concrete class. 
                               it contains all the data needed to fill a Dockerfile Template


      RuntimeSourceFeedVagrant: it is a concrete class.
                                it contains all the data needed to fill a Vagrantfile Template

------------------------


      RuntimeSource: 

            it is an abstract class and defines the interface for all the concrete RuntimeSource objects
            RuntimeSourceDocker,RuntimeSourceVagrant

            A runtime source concrete object is created by a RuntimeSourceCreator factory object from:
            1. A RuntimeSourceTemplate concrete object (template)
            2. A RuntimeSourceFeed concrete object     (data filling the gaps)
            We'll use jinja2 for templating.


      RuntimeSourceDocker: it is a concrete class. 
                           it implements RuntimeSource's interface. 
                           it represents a Dockerfile


      RuntimeSourceVagrant: it is a concrete class. 
                            it implements RuntimeSource's interface. 
                            it represents a Vagranfile

------------------------

      RuntimeSourceTemplate: it is an abstract class.
                             it defines the interface for the templates object instances
                             RuntimeSourceTemplateDocker, RuntimeSourceTemplateVagrant


      RuntimeSourceTemplateDocker: 

      RuntimeSourceTemplateVagrant:

--------------------------


      RuntimeSourceCreator: it declares the factory method that creates a RuntimeSource object
                            In order to create a RuntimeSourceObject it needs:
                            1. A RuntimeSourceTemplate concrete object (template)
                            2. A RuntimeSourceFeed concrete object     (data filling the gaps)


      RuntimeSourceCreator: it defines the interface for the concrete runtime creator objects: 

      RuntimeSourceCreatorDocker: concrete creator for RuntimeSourceDocker objects
                                  it overrides the RuntimeSourceCreator's factory method.
                                  it to create a concrete RuntimeSourceDocker instance.

      RuntimeSourceCreatorVagrant: concrete creator for RuntimeSourceVagrant objects.
                                   it overrides the RuntimeSourceCreator's factory method 
                                   it creates a concrete RuntimeSourceVagrant instance.

-----------------------------

Factory Method's actors

* Product: RuntimeSource
* ConcreteProduct: RuntimeSourceDocker, RuntimeSourceVagrant
* Crator: RuntimeSourceCreator
* ConcreteCreator : RuntimeSourceCreatorDocker, RuntimeSourceCreatorVagrant

------------------------------

# What does teaster do for you?
1. accept requests to create the couple (runtime environment, provisioning environment) and publish that one somewhere
2. accept requests to create the tuple  (runtime environment, provisioning environment, reproducer). So it create an automation env and make it available to the tester.

# Who create the couple and the triple? Consumer!
it's a consumer.
A consumer get in input a request for an environment and works to produce in output the required env.
A consumer knows how to handle only a specific product. So sle15 and sle12sp3 need two different consumer.

# What Does a consumer know?

* a source

  it contain infos to create the required environment.
  
  For example:
  
  if the required env is a container a source will be the url for a Dockerfile
  if the required env is a vm it will be the Vagranfile
  (Docker is a specifi instance of a container runtime env and Vagrant it is for vm runtime env.
   any instance of a runtime env cuold be taken in consideration)
   
* a destination
  
  an url to build the environment.
  
  For example:
  
  if the required env is a container, a url will point to a service that will build the image (from the 
  Dockerfile) for us.
  
# The builder

it builds our environment, it is bound to the url knokn by the consumer.
It get infos (Dockerfile, Vagrantfile) from the consumer.

  For example:
  
  * docker builder
  * vagrant builder
  
  
# Set up dev environment

1. `pip install virtualenvwrapper`

2. `mkdir $HOME/dev`

3. `sudo find / -name virtualenvwrapper.sh`

4. Add three lines to your shell startup file (.bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package:

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/dev
source /usr/local/bin/virtualenvwrapper.sh # use the path obtained at point 3
```

5. `cd $HOME/dev; git clone https://github.com/kinderp/teaster.git; cd $HOME/dev/teaster`

6. `mkvirtualenv teaster`

Activate and deativate your env using `workon` and `deactivate` commands, see here for details https://virtualenvwrapper.readthedocs.io/en/latest/install.html

# Set up the infrastructure

1. Install docker and docker-compose
2. cd `$HOME/dev/teaster`
3. `docker-compose up`
