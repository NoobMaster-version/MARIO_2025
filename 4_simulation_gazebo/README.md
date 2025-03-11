# MARIO ROS2 - Manipulator Arm Robot Simulation

This repository contains a ROS2 package for simulating a 5-DOF robotic manipulator in Gazebo. The package provides functionality for both forward kinematics (control robot joints to achieve a specific end-effector position) and inverse kinematics (calculate joint positions to reach a desired point in space).

<p align="center">
  <img src="assets/gazebo.png" width="800" alt="MARIO Manipulator in Gazebo"/>
</p>

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
  - [Launching the Simulation](#launching-the-simulation)
  - [Forward Kinematics](#forward-kinematics)
  - [Inverse Kinematics](#inverse-kinematics)
- [Project Structure](#project-structure)
- [Theory Overview](#theory-overview)
- [Troubleshooting](#troubleshooting)

## Dependencies

### ROS2 and System Requirements
- Ubuntu 22.04 (recommended)
- ROS2 Humble Hawksbill
- Gazebo Ignition (Garden)
- Python 3.10+

### ROS2 Packages
```bash
# Core ROS2 packages
sudo apt install ros-humble-desktop-full

# Gazebo/Ignition integration
sudo apt install ros-humble-ros-ign ros-humble-ign-ros2-control

# ROS2 Control packages
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers \
                 ros-humble-joint-state-broadcaster \
                 ros-humble-joint-trajectory-controller \
                 ros-humble-forward-command-controller
```

## Installation

1. **Create a ROS2 workspace** (if you don't already have one):
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/NoobMaster-version/MARIO_2025.git
   ```

3. **Build the workspace**:
   ```bash
   cd ~/ros2_ws
   colcon build
   ```

4. **Source the workspace**:
   ```bash
   source ~/ros2_ws/install/setup.bash
   # Add this line to your ~/.bashrc to automatically source the workspace
   echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
   ```

## Usage

### Launching the Simulation

To start the Gazebo simulation environment with the MARIO manipulator:

```bash
ros2 launch simulation_gazebo basic_gazebo.launch.py
```

This will:
1. Launch the Gazebo simulator
2. Spawn the MARIO robot model
3. Start the required controllers

### Forward Kinematics

Forward kinematics allows you to control the robot by specifying joint angles and observe the resulting end-effector position:

```bash
ros2 run simulation_gazebo forward_kinematics.py
```

You will be prompted to enter angles for the base, shoulder, and elbow joints, as well as gripper state. The program will calculate and display the resulting end-effector position.

### Inverse Kinematics

Inverse kinematics lets you specify a desired position for the end-effector, and the program calculates the required joint angles:

```bash
ros2 run simulation_gazebo inverse_kinematics.py
```

You will be prompted to enter the desired x, y, and z coordinates. The program will calculate the joint angles needed to reach that position and move the robot accordingly.

## Project Structure

```
simulation_gazebo/
├── config/                 # Controller and position configurations
├── launch/                 # Launch files for Gazebo and robot
├── meshes/                 # STL files for robot visualization
├── rviz/                   # Configuration for RViz visualization
├── scripts/                # Python scripts for kinematics
│   ├── forward_kinematics.py
│   ├── forward_kinematics_module.py
│   ├── inverse_kinematics.py
│   └── inverse_kinematics_module.py
├── urdf/                   # Robot description files
├── CMakeLists.txt          # Build configuration
└── package.xml             # Package metadata and dependencies
```

## Theory Overview

The robot manipulator uses the Denavit-Hartenberg (DH) parameters for kinematic calculations:

```
+-----------------------+--------------+--------------+----------+--+
| Transformation Matrix |              |              |          |  |
+-----------------------+--------------+--------------+----------+--+
| cosθ                  | -cosα * sinθ | sinα * sinθ  | a * cosθ |  |
| sinθ                  | cosα * cosθ  | -sinα * cosθ | a * sinθ |  |
| 0                     | sinα         | cosα         | d        |  |
| 0                     | 0            | 0            | 1        |  |
+-----------------------+--------------+--------------+----------+--+
```

DH parameters for the MARIO manipulator:
```
+-------------------+-----------------------------+------------------+-----------------------------+
|  θ (about Z axis) |      d (along Z axis)       | α (about X axis) |      a (along X axis)       |
+-------------------+-----------------------------+------------------+-----------------------------+
| theta_base        | d0 (base to shoulder - 2.5) | π/2              | 0                           |
| theta_shoulder    | 0                           | 0                | a1 (shoulder to elbow - 12) |
| theta_elbow       | 0                           | π/2              | 0                           |
| 0                 | d3 (elbow to end - 9.5)     | 0                | 0                           |
+-------------------+-----------------------------+------------------+-----------------------------+
```

## Troubleshooting

### Common Issues

1. **Gazebo not launching properly**:
   - Make sure Gazebo is installed correctly
   - Check if environment variables are set properly
   ```bash
   # Check Gazebo plugin path
   echo $GAZEBO_PLUGIN_PATH
   ```

2. **Robot not moving**:
   - Verify controllers are running:
   ```bash
   ros2 control list_controllers
   ```
   - Check for errors in the terminal where you launched Gazebo

3. **Package not found**:
   - Make sure you've sourced your workspace:
   ```bash
   source ~/ros2_ws/install/setup.bash
   ```

4. **Kinematics errors**:
   - Ensure your input values are within the robot's reach
   - The robot has physical limits on joint movements (0 to 180 degrees)

### Reporting Issues

If you encounter any problems not addressed above, please open an issue on the repository with:
- Description of the problem
- Steps to reproduce
- Terminal output/error messages
- Your system configuration

## License

This package is licensed under the MIT License - see the LICENSE file for details.

---

Created by Society of Robotics and Automation, VJTI.

