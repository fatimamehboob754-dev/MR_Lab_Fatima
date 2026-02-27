Brief Description: This lab focused on onboarding with the Linux terminal environment and setting up a ROS 2 Humble development workspace. The primary goal was to understand the core concepts of ROS 2—including nodes, topics, packages, and workspaces—by creating a Python-based package named my_first_pkg. The lab culminated in writing and executing a custom Python node (simple_node) that logs messages to the terminal.

Commands used:
pwd: Print working directory.
ls: List directory contents.
cd: Change directory.
mkdir -p: Create directories, including parent directories if they don't exist.
nano: A beginner-friendly terminal text editor used to edit files.
ros2 --version: Command to verify the ROS 2 installation and check availability.
source: Used to execute the setup files to update environment variables.
printenv | grep: Used to confirm specific environment variables like ROS or AMENT.
colcon build: The command used to build and compile the workspace.
echo: Used to append sourcing commands to the .bashrc file for persistence.
ros2 pkg create: Used to create a new ROS 2 package with a specific build type.
ros2 pkg list: Used to list all available ROS 2 packages.
grep: Used to filter command output for specific text.
chmod +x: Used to make the Python node file executable.
ros2 run: The command used to execute a specific node from a package.
ros2 node list: Used to see a list of currently running nodes.
sudo apt update / install: Linux package management commands used for troubleshooting missing tools like colcon.

Problems Faced and Solutions
  Problem: ros2: command not found 
     During the initial setup, I encountered an issue where the terminal returned a ros2: command not found error when attempting to verify the installation with ros2 --version. This occurred because the ROS 2 environment variables had not yet been loaded into the current terminal session. I resolved this by executing source /opt/ros/humble/setup.bash, which updated the terminal's path and allowed it to correctly locate the ROS 2 executables. 
  
 Reflection:
 This lab was a valuable introduction to the ROS 2 ecosystem and the essential nature of the Linux terminal. I learned that workspaces are not just folders, but structured environments that require consistent building and sourcing to function. Encountering the "command not found" error was a key learning moment, as it taught me how environment variables bridge the gap between installed software and active terminal sessions. Understanding the role of setup.py in registering entry points helped demystify how Python scripts become executable ROS 2 nodes. Overall, these tasks built the fundamental skills needed to manage more complex, multi-node robotic systems in the future.
