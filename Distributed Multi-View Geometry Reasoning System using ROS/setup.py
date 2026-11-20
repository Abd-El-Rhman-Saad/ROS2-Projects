from setuptools import setup

package_name = 'multi_view_geometry'

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
    description='ROS 2 Jazzy package for multi_view_geometry',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_stream_node = multi_view_geometry.camera_stream_node:main',
            'keypoint_detection_node = multi_view_geometry.keypoint_detection_node:main',
            'descriptor_extraction_node = multi_view_geometry.descriptor_extraction_node:main',
            'feature_matching_node = multi_view_geometry.feature_matching_node:main',
            'geometric_consistency_node = multi_view_geometry.geometric_consistency_node:main',
            'motion_estimation_node = multi_view_geometry.motion_estimation_node:main',
            'reliability_decision_node = multi_view_geometry.reliability_decision_node:main',
        ],
    },
)
