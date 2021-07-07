#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from os.path import dirname
from os.path import join

from setuptools import setup


def read(fname):
    return open(join(dirname(__file__), fname)).read()


setup(
    name='aabbtree',
    version='2.8.1',
    license='MIT',
    description='Pure Python implementation of d-dimensional AABB tree.',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    author='Kenneth (Kip) Hart',
    author_email='kiphart91@gmail.com',
    url='https://github.com/kip-hart/AABBTree',
    project_urls={
        'Documentation': 'https://aabbtree.readthedocs.io',
    },
    py_modules=['aabbtree'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords=[
        'aabb',
        'aabb tree',
        'binary tree'
    ],
)
