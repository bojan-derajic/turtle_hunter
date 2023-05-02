from setuptools import find_packages
from setuptools import setup

setup(
    name='turtle_hunter_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('turtle_hunter_interfaces', 'turtle_hunter_interfaces.*')),
)
