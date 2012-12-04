#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


APP_NAME = 'adventure'
APP_SCRIPT = './adventure'
VERSION = '0.0.1'


# Grab requirments.
with open('requirementss.txt') as f:
    required = f.readlines()


settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


settings.update(
    name=APP_NAME,
    version=VERSION,
    description='Git for Humans.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/legit',
    packages= ['legit',],
    install_requires=required,
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'legit = legit.cli:main',
        ],
    }
)



setup(**settings)
