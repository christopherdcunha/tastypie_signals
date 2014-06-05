#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tastypie_signals',
    version='0.1.0',
    description='Tastypie Signals emits convenient django signals from your Tastypie resources.',
    long_description=readme + '\n\n' + history,
    author='Christopher D\'Cunha',
    author_email='me@christopherdcunha.com',
    url='https://github.com/christopherdcunha/tastypie_signals',
    packages=[
        'tastypie_signals',
    ],
    package_dir={'tastypie_signals':
                 'tastypie_signals'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tastypie_signals',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
