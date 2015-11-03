#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement
import os
import sys
import codecs
from setuptools import setup

# Change to source's directory prior to running any command
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    # We're most likely being frozen and __file__ triggered this NameError
    # Let's work around that
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)


def read(fname):
    '''
    Read a file from the directory where setup.py resides
    '''
    file_path = os.path.join(SETUP_DIRNAME, fname)
    with codecs.open(file_path, encoding='utf-8') as rfh:
        return rfh.read()


_LOCALS = {}
try:
    # Version info -- read without importing
    with open(os.path.join(SETUP_DIRNAME, 'pytest_logging', 'version.py')) as rfh:
        exec(rfh.read(), None, _LOCALS)  # pylint: disable=exec-used
except IOError:
    # tox egg_info on a zip of this code!? Let's resort to importing
    sys.path.insert(0, SETUP_DIRNAME)
    from pytest_logging.version import __version__
    _LOCALS['__version__'] = __version__


VERSION = _LOCALS['__version__']
LONG_DESCRIPTION = read('README.rst')

setup(
    name='pytest-logging',
    version=VERSION,
    author='Pedro Algarvio',
    author_email='pedro@algarvio.me',
    maintainer='Pedro Algarvio',
    maintainer_email='pedro@algarvio.me',
    license='MIT',
    url='https://github.com/saltstack/pytest-logging',
    description='Configures logging and allows tweaking the log level with a py.test flag',
    long_description=LONG_DESCRIPTION,
    py_modules=['pytest_logging'],
    install_requires=['pytest>=2.8.1'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'logging = pytest_logging.plugin',
        ],
    },
)
