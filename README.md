# teaster

Teaster: automate your dirty tester work and take time for a relaxing tea.

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
  
  
