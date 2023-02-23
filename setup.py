from setuptools import find_packages, setup

setup(
    name='encrypt',
    packages=find_packages(include=['encrypt']),
    version='1.0.0',
    description='Quick encryption with password',
    author='Espen Kirkesæther Brun',
    license='MIT',
    install_requires=['scrypt'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    test_suite='tests',
)
