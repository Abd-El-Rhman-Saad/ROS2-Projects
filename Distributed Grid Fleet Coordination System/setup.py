from setuptools import setup

package_name = 'fleet_coordination'

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
    description='ROS 2 Jazzy distributed grid fleet coordination package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'task_manager = fleet_coordination.task_manager:main',
            'traffic_controller = fleet_coordination.traffic_controller:main',
            'vehicle_node = fleet_coordination.vehicle_node:main',
            'monitor_node = fleet_coordination.monitor_node:main',
        ],
    },
)
