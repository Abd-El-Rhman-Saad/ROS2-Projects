from setuptools import setup

package_name = 'navigation_hint_system'

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
    description='ROS 2 Jazzy package for navigation_hint_system',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_stream_node = navigation_hint_system.camera_stream_node:main',
            'object_detection_node = navigation_hint_system.object_detection_node:main',
            'depth_estimation_node = navigation_hint_system.depth_estimation_node:main',
            'feature_extraction_node = navigation_hint_system.feature_extraction_node:main',
            'motion_tracking_node = navigation_hint_system.motion_tracking_node:main',
            'visual_odometry_node = navigation_hint_system.visual_odometry_node:main',
            'navigation_node = navigation_hint_system.navigation_node:main',
            'action_execution_node = navigation_hint_system.action_execution_node:main',
        ],
    },
)
