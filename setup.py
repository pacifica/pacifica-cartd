#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Setup and install the cart."""
try:  # pip version 9
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

setup(
    name='PacificaCartd',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Pacifica Cartd',
    author='David Brown',
    author_email='david.brown@pnnl.gov',
    packages=find_packages(),
    scripts=['CartServer.py', 'DatabaseCreate.py'],
    entry_points={
        'console_scripts': ['CartServer=cart.__main__:main']
    },
    install_requires=[str(ir.req) for ir in INSTALL_REQS]
)
