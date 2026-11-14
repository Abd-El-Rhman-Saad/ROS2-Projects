from setuptools import find_packages, setup

package_name = 'navigation_hint_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nada',
    maintainer_email='nada@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_stream_node = navigation_hint_system.camera_stream_node:main',
            'object_detection_node = navigation_hint_system.object_detection_node:main',
            'depth_estimation_node = navigation_hint_system.depth_estimation_node:main',
            'feature_extraction_node = navigation_hint_system.feature_extraction_node:main',
            'motion_tracking_node = navigation_hint_system.motion_tracking_node:main',
            'visual_odometry_node = navigation_hint_system.visual_odometry_node:main',
            'navigation__decision_node = navigation_hint_system.navigation_decision_node:main',
            'action_excution_node = navigation_hint_system.action_execution_node:main',
        ],
    },
)
