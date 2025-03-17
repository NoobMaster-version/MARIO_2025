# Table of Contents
* [Steps to run the demo in Gazebo Harmonic](#steps-to-run-the-demo-in-gazebo-harmonic) 
* [Steps For Running the Scripts in Gazebo Harmonic](#steps-for-running-the-scripts-in-gazebo-harmonic)

## Steps to run the demo in Gazebo Harmonic
* Gazebo Harmonic is the simulation tool that is used by ROS2 Jazzy. It has a lot of Applications. In this workshop we will be using ROS2 to simulate the Manipulator. For running the simulation just follow commands mentioned below.
* If you have not installed the joint_state_publishers and ros_control for ROS2 Jazzy, follow the commands given below:

```bash
sudo apt update
sudo apt install ros-jazzy-joint-state-publisher ros-jazzy-ros2-control ros-jazzy-ros2-controllers ros-jazzy-gz-ros2-control
```

*  Run the launch file

Make sure you have sourced your workspace before running this command.
```bash
ros2 launch simulation_gazebo basic_gazebo.launch.py
```

To source your workspace follow the steps mentioned below.
<p align="center">
  <img src="../assets/gazebo.png" width="800"/>
</p>


### Steps For Running the Scripts in Gazebo Harmonic
We will be testing out 2 scripts (forward_kinematics.py, inverse_kinematics.py).

Firstly copy the 4_simulation_gazebo folder to src folder in your workspace using command (in fresh terminal) :

```bash
cp -r MARIO/4_simulation_gazebo Ros2_ws/src
```
Now source ROS2. Use following commands in your workspace :

```bash
source /opt/ros/jazzy/setup.bash
```
Now we build simulation_gazebo package using this command:

```bash
colcon build
```
Now we source the workspace using following command :
```bash
source install/setup.bash
```
For running the scripts on Gazebo Harmonic, firstly launch the simulation using the command:

```bash
ros2 launch simulation_gazebo basic_gazebo.launch.py
```

After starting Gazebo Harmonic we will be testing out `forward kinematics.py`.
Open a fresh terminal and navigate to your workspace. Now source the workspace and run forward_kinematics.py using following commands : 

```bash
source install/setup.bash
ros2 run simulation_gazebo forward_kinematics.py
```
Similarly, you can test out the script for `inverse_kinematics.py`.
