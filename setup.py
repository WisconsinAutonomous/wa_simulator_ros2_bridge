from setuptools import setup

package_name = 'wa_simulator_ros2_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wisconsinautonomous',
    maintainer_email='wisconsinautonomous@studentorg.wisc.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "bridge = wa_simulator_ros2_bridge.bridge:main",
        ],
    },
)
