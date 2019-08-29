#!/usr/bin/env python

import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('shenjian/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='shenjian',
    version=version,
    description='shenjian rest sdk',
    long_description=readme,
    packages=['shenjian'],
    install_requires=['requests!=2.9.0'],
    include_package_data=True,
    url='http://www.shenjian.io',
)