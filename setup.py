from setuptools import find_packages, setup

setup(
    name='encrypt',
    packages=find_packages(include=['encrypt']),
    version='0.1.0',
    description='Quick encryption with password and salt',
    author='Espen Kirkesæther Brun',
    license='MIT',
    install_requires=['cryptography'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    test_suite='tests',
)
