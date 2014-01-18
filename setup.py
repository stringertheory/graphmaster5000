#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import graphmaster

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'graphmaster',
]

requires = []

with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='graphmaster5000',
    version=graphmaster.__version__,
    description="Doesn't do anything yet.",
    long_description=readme + '\n\n' + history,
    author='Mike Stringer',
    author_email='mike.stringer@datascopeanalytics.com',
    url='https://github.com/stringertheory/graphmaster5000',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'graphmaster': 'graphmaster'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Crap',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
    ),
)
