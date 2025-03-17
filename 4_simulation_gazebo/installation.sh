#!/bin/bash

set -e  # Exit on error

echo "======================================================================"
echo "Installing ROS 2 Jazzy, Gazebo Harmonic and required dependencies"
echo "======================================================================"

# Function to check if a command executed successfully
check_success() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed. Exiting."
        exit 1
    fi
}

# Update package lists
echo "Updating package lists..."
sudo apt update
check_success "apt update"

# Install essential tools
echo "Installing essential tools..."
sudo apt install -y software-properties-common curl gnupg lsb-release build-essential cmake git
check_success "installing essential tools"

# Set locale
echo "Setting up locale..."
sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
check_success "setting locale"

# Add ROS 2 repository
echo "Adding ROS 2 repository..."
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
check_success "adding ROS 2 repository"

# Add Gazebo repository
echo "Adding Gazebo repository..."
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
check_success "adding Gazebo repository"

# Update package lists again
echo "Updating package lists with new repositories..."
sudo apt update
check_success "updating package lists"

# Install ROS 2 Jazzy
echo "Installing ROS 2 Jazzy Desktop..."
sudo apt install -y ros-jazzy-desktop
check_success "installing ROS 2 Jazzy Desktop"

# Install Gazebo Harmonic
echo "Installing Gazebo Harmonic..."
sudo apt install -y gz-harmonic
check_success "installing Gazebo Harmonic"

# Install ROS 2 development tools
echo "Installing ROS 2 development tools..."
sudo apt install -y ros-jazzy-ros-base python3-colcon-common-extensions python3-rosdep python3-vcstool
check_success "installing ROS 2 development tools"

# Initialize rosdep
echo "Initializing rosdep..."
sudo rosdep init || true  # May fail if already initialized
rosdep update
check_success "updating rosdep"

# Install ROS 2 Control packages
echo "Installing ROS 2 Control packages..."
sudo apt install -y ros-jazzy-ros2-control ros-jazzy-ros2-controllers
check_success "installing ROS 2 Control"

# Install Gazebo ROS packages
echo "Installing Gazebo-ROS integration packages..."
sudo apt install -y ros-jazzy-ros-gz ros-jazzy-ros-gz-bridge ros-jazzy-ros-gz-sim
check_success "installing Gazebo-ROS integration"

# Install additional packages specific to the project
echo "Installing additional project dependencies..."
sudo apt install -y \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-joint-state-broadcaster \
    ros-jazzy-joint-trajectory-controller \
    ros-jazzy-forward-command-controller \
    ros-jazzy-gazebo-ros2-control \
    ros-jazzy-controller-manager \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-xacro \
    ros-jazzy-rviz2 \
    ros-jazzy-gz-ros2-control
check_success "installing additional dependencies"

# Print success message
echo "======================================================================"
echo "Installation complete!"
echo ""
echo "To use ROS 2 Jazzy, run the following command in each terminal:"
echo "  source /opt/ros/jazzy/setup.bash"
echo ""
echo "Create a ROS 2 workspace and clone the simulation_gazebo package:"
echo "  mkdir -p ~/ros2_ws/src"
echo "  cd ~/ros2_ws/src"
echo "  # Clone your simulation_gazebo package here"
echo "  cd ~/ros2_ws"
echo "  colcon build"
echo "  source ~/ros2_ws/install/setup.bash"
echo ""
echo "To test Gazebo Harmonic, run:"
echo "  gz sim"
echo ""
echo "To launch the simulation_gazebo package:"
echo "  ros2 launch simulation_gazebo basic_gazebo.launch.py"
echo "======================================================================"
