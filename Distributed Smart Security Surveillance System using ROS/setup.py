from setuptools import find_packages, setup

package_name = 'smart_security_system'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abd El-Rhman Muhammad Saad',
    maintainer_email='abdelrhmanmsaad22@gmail.com',
    description='ROS 2 Jazzy package for smart_security_system',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_stream_node = nodes.camera_stream_node:main',
            'object_detection_node = nodes.object_detection_node:main',
            'depth_estimation_node = nodes.depth_estimation_node:main',
            'scene_analyzer = nodes.Scene_Analysis_Node:main',
            'event_manager = nodes.event_manager_node:main',
            'security_response_node = nodes.security_response_node:main',
            'event_logger = nodes.event_logger_node:main',
            'system_monitor = nodes.SystemMonitorNode:main',
        ],
    },
)
