from setuptools import setup

package_name = 'smart_security_system'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    package_dir={package_name: 'nodes'},
    data_files=[
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
            'camera_stream_node = smart_security_system.camera_stream_node:main',
            'object_detection_node = smart_security_system.object_detection_node:main',
            'depth_estimation_node = smart_security_system.depth_estimation_node:main',
            'scene_analyzer = smart_security_system.Scene_Analysis_Node:main',
            'event_manager = smart_security_system.event_manager_node:main',
            'security_response_node = smart_security_system.security_response_node:main',
            'event_logger = smart_security_system.event_logger_node:main',
            'system_monitor = smart_security_system.SystemMonitorNode:main',
        ],
    },
)
