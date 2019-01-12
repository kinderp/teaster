# teaster
Teaster: automate your dirty tester work and take time for a relaxing tea.

# Introduction

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
   
    - runtime env 
    - all the provisioned software (before or after) 
    - reproducer
   
   An automation environment can be represented by a tuple:
   
   `(runtime env, provisioned software, reproducer)`
   
   All the possible combinations of these three components create an automation environment:
   
   Cli automation environments
    * (container, package before update, script bash)
    * (container, package after update, script bash)
    * (container + openqa instance, package before update, openqa testmodule)
    * (cotaniner + openqa instance, package after  update, openqa testmodule)
    * (vm, package before update, script bash)
    * (vm, package after  update, script bash)
    * (vm + openqa instance, package before update, openqa testmodule)
    * (vm + openqa instance, package after  update, openqa testmodule)

   Gui automation environments
    * (container + openqa instance, package before update, openqa testmodule + needles)
    * (cotaniner + openqa instance, package after  update, openqa testmodule + needles)
    * (vm + openqam instance, package before update, openqa testmodule + needles)
    * (vm + openqa instance, package after  update, openqa testmodule + needles)
    
2. Provisioning of the runtime environment (and installation tests)

    We need to be sure that the packages we are testing can be installed on top of our runtime environment.
    We are helped on that by tool like mtui but sometimes it needs some manual work and anyway it's not a completely automated process.
    
3. Reproducing 

   Reproduce the bug before and after (update and downgrade)
   Even in this phase mtui is our friend.
   
4. Comparison

   
In this scenario just only the first phase: the mental process to figure out the better reproducer
really required an human intellectual intervention.

The same reproducer is applied (manually) for different products. So all the steps of the entire process
are repeated by testers with a lof of wasting time.

As a tester before going through all the entire process i want:

Know if a tester has already worked on that bug, in other words if a reproducer for that particul bug already exists for other products. (We do that manually searching for a bug in qam.suse)

  if it's the first time that bug is tested (no reproducer for that bug)

    1. Concentrate just only on the reproducer
    2. Get automagically a runtime environment with the testing package installed (provisioning)
    3. Once finished creating the reproducer push that one in a repository and share with all other testers in the future
    
  if a reproducer already exists:
    
    1. Get automagically an automation environment with the testing package installed (provisioning) and the reproducer ready to be executed
    2. Chose the runtime environment i like (container or vm)
    3. Run the reproducer  (before and after)
    4. Compare the results (before and after)
