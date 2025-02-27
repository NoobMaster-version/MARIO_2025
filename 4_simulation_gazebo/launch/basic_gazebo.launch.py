#!/usr/bin/python3

# -*- coding: utf-8 -*-
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_prefix

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('ros_gz_sim')
    pkg_mario_bot = get_package_share_directory('simulation_gazebo')
    # We get the whole install dir
    description_package_name = "simulation_gazebo"
    install_dir = get_package_prefix(description_package_name)
    # Set the path to the WORLD model files
    gazebo_models_path = os.path.join(pkg_mario_bot, 'models')
    
    if 'GZ_SIM_RESOURCE_PATH' in os.environ:
        os.environ['GZ_SIM_RESOURCE_PATH'] =  os.environ['GZ_SIM_RESOURCE_PATH'] + ':' + install_dir + '/share' + ':' + gazebo_models_path
    else:
        os.environ['GZ_SIM_RESOURCE_PATH'] = install_dir + "/share:" + gazebo_models_path
    if 'GZ_SIM_RESOURCE_PATH' in os.environ:
        os.environ['GZ_SIM_RESOURCE_PATH'] = os.environ['GZ_SIM_RESOURCE_PATH'] + ':' + install_dir + '/lib'
    else:
        os.environ['GZ_SIM_RESOURCE_PATH'] = install_dir + '/lib'

    print("GAZEBO MODELS PATH=="+str(os.environ["GZ_SIM_RESOURCE_PATH"]))
    print("GAZEBO PLUGINS PATH=="+str(os.environ["GZ_SIM_RESOURCE_PATH"]))
    
    # Direct Gazebo launch (without world specification - will use default empty world)
    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', '--gui'],
        output='screen'
    )
    
    # model launch
    mario = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_mario_bot, 'launch', 'mario.launch.py'),
        )
    )   
    return LaunchDescription([  
        gazebo,
        mario
    ])