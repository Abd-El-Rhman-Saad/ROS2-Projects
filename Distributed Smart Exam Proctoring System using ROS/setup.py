from setuptools import setup

package_name = 'exam_proctoring_system'

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
    description='ROS 2 Jazzy package for exam_proctoring_system',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_stream_node = exam_proctoring_system.camera_stream_node:main',
            'object_detection_node = exam_proctoring_system.object_detection_node:main',
            'depth_estimation_node = exam_proctoring_system.depth_estimation_node:main',
            'behavior_analysis_node = exam_proctoring_system.behavior_analysis_node:main',
            'alert_action_node = exam_proctoring_system.alert_action_node:main',
        ],
    },
)
