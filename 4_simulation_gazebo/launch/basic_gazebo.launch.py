#!/usr/bin/python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_prefix
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_mario_bot = get_package_share_directory('simulation_gazebo')

    # We get the whole install dir
    description_package_name = "simulation_gazebo"
    install_dir = get_package_prefix(description_package_name)

    # Set the path to the world file
    world_file = PathJoinSubstitution([FindPackageShare(description_package_name), 'worlds', 'empty.sdf'])

    # Launch Gazebo Harmonic with ROS 2 bridge
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items(),
    )

    # Launch the robot
    mario = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_mario_bot, 'launch', 'mario.launch.py'),
        )
    )

    # Bridge between ROS 2 and Gazebo
    bridge = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_bridge.launch.py'),
        )
    )

    return LaunchDescription([
        gz_sim,
        mario,
        bridge
    ])
