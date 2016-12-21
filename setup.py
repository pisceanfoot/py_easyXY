#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# packages = [
#     'py_easyXY'
# ]

requires = ['requests']

with open('py_easyXY/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='py_easyXY',
    version=version,
    description='Common Python Share for Humans.',
    long_description=readme,
    author='Leo He',
    author_email='pisceanfoot@gmail.com',
    url='https://github.com/pisceanfoot/py_easyXY',
    packages=find_packages(),
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    )
)
