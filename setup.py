from setuptools import setup, find_packages
import sys

setup(
    name="plumb_util",
    version = '0.1',
    maintainer='Luminoso, LLC',
    maintainer_email='dev@lumino.so',
    license = "Proprietary",
    url = 'http://github.com/LuminosoInsight/plumbing',
    platforms = ["any"],
    description = "Plumbing utility library",
    packages=find_packages(),
    install_requires=['dnspython'],
)
