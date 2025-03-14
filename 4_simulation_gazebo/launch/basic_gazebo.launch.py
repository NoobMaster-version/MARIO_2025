#!/usr/bin/python3

# -*- coding: utf-8 -*-
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_prefix
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_mario_bot = get_package_share_directory('simulation_gazebo')
   
    description_package_name = "simulation_gazebo"
    install_dir = get_package_prefix(description_package_name)
    
    gazebo_models_path = os.path.join(pkg_mario_bot, 'models')
    
    if 'GZ_SIM_RESOURCE_PATH' in os.environ:
        os.environ['GZ_SIM_RESOURCE_PATH'] = os.environ['GZ_SIM_RESOURCE_PATH'] + ':' + install_dir + '/share' + ':' + gazebo_models_path
    else:
        os.environ['GZ_SIM_RESOURCE_PATH'] = install_dir + "/share" + ':' + gazebo_models_path
    
    if 'GZ_SIM_SYSTEM_PLUGIN_PATH' in os.environ:
        os.environ['GZ_SIM_SYSTEM_PLUGIN_PATH'] = os.environ['GZ_SIM_SYSTEM_PLUGIN_PATH'] + ':' + install_dir + '/lib'
    else:
        os.environ['GZ_SIM_SYSTEM_PLUGIN_PATH'] = install_dir + '/lib'

    print("GAZEBO MODELS PATH=="+str(os.environ["GZ_SIM_RESOURCE_PATH"]))
    print("GAZEBO PLUGINS PATH=="+str(os.environ["GZ_SIM_SYSTEM_PLUGIN_PATH"]))
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )
    
    mario = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_mario_bot, 'launch', 'mario.launch.py'),
        )
    )
    
    return LaunchDescription([
        gazebo,
        mario
    ])
