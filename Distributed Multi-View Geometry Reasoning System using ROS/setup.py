from setuptools import find_packages, setup

package_name = 'multi_view_geometry'

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
    description='ROS 2 Jazzy package for multi_view_geometry',
    license='MIT',
    entry_points={
        'console_scripts': [
            'keypoint_detection_node = nodes.keypoint_detection_node:main',
            'descriptor_extraction_node = nodes.descriptor_extraction_node:main',
            'feature_matching_node = nodes.feature_matching_node:main',
            'geometric_consistency_node = nodes.geometric_consistency_node:main',
            'motion_estimation_node = nodes.motion_estimation_node:main',
            'reliability_decision_node = nodes.reliability_decision_node:main',
        ],
    },
)
