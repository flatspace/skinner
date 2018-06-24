#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_requirements(file):
    parsed_requirements = parse_requirements(file, session=PipSession())
    return [str(ir.req) for ir in parsed_requirements]


setup(
    name='skinner',
    version='0.0.0',
    description="Utilities for deep reinforcement learning",
    author="Brecht Dierckx",
    author_email='brecht.dierckx@gmail.com',
    url='https://github.com/flatspace/skinner',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    zip_safe=False,
    keywords='skinner',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    test_suite='tests',
    repository='http://www.python.org/pypi/'
    #tests_require=get_requirements('requirements_text.txt')
)
