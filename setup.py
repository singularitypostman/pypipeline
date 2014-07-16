#!/usr/bin/env python
#
# Example usage
# - Install:
#   python setup.py install
# - Build an egg:
#   python setup.py bdist_egg
#
# We use the setup tools import as opposed to the standard "from
# distutils.core import setup" in order to add the bdist_egg command.
#

from setuptools import setup

setup(
    name='pypipeline',
    version='0.1',
    description='Python scripts for running pipelines of experiments locally or on Sun Grid Engine.',
    author='Matt Gormley',
    author_email='mrg@cs.jhu.edu',
    url='http://www.cs.jhu.edu/~mrg/',
    packages=['pypipeline'])