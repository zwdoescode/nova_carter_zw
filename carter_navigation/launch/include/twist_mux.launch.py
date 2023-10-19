# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
import os

from ament_index_python.packages import get_package_share_directory

from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch.actions import DeclareLaunchArgument
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    mux_config = LaunchConfiguration('mux_config')
    mux_config_arg = DeclareLaunchArgument('mux_config', default_value=
    os.path.join(get_package_share_directory('carter_navigation'), 'params', 'mux.yaml'))
    cmd_vel = LaunchConfiguration('cmd_vel')
    cmd_vel_arg = DeclareLaunchArgument('cmd_vel', default_value='/mux/cmd_vel')

    twist_mux_node = Node(
        package='twist_mux',
        executable='twist_mux',
        remappings={('/cmd_vel_out', LaunchConfiguration('cmd_vel'))},
        parameters=[{
            mux_config,
        }])

    return LaunchDescription([
        mux_config_arg,
        cmd_vel_arg,
        twist_mux_node
    ])