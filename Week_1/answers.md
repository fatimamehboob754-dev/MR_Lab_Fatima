Answer 1: Node: A process that performs computation and communicates with other processes in the ROS graph.
Topic: A named bus over which nodes exchange messages using a publish-subscribe model.
Package: The fundamental unit of software organization in ROS 2 that contains your code, data, and configuration files.
Workspace: A directory structure that houses multiple ROS 2 packages and provides the environment for building and running them.

Answer 2: Sourcing is required to update your terminal's environment variables so the system knows where to find ROS 2 commands and your custom packages. 
What happens if you don't source: Your terminal will not recognize ROS 2 commands and it will be unable to locate or execute any nodes within your workspace.

Answer 3: The purpose of colcon build is to compile the source code, resolve dependencies, and prepare the environment so that your packages are ready to be executed.
It generates the following three folders in your workspace:build, install, log.

Answer 4: The entry_points console script acts as a map that tells the system which Python function to execute when you call a specific command. Essentially, it links a "friendly name" (the command you type in the terminal) to a specific main() function inside your script so that ROS 2 can launch your node.

Answer 5: 
 +------------+                 +-----------+                +------------+
 |            |      Topic      |           |                |            |
 |  Node A    |---------------->|  /chatter |--------------->|  Node B    |
 | (Publisher)|     (Message)   |           |    (Message)   |(Subscriber)|
 +------------+                 +-----------+                +------------+
