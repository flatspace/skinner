#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


with open('requirements.txt') as req_file:
    requirements = req_file.read().splitlines()
with open('requirements_test.txt') as req_file_test:
    test_requirements = req_file_test.read().splitlines()


setup(
    name='skinner',
    version='0.0.0',
    description="Utilities for deep reinforcement learning",
    long_description=readme + '\n\n' + history,
    author="flatspaceking",
    author_email='flatspaceking@gmail.com',
    url='https://github.com/flatspace/skinner',
    packages=[
        'skinner',
    ],
    package_dir={'skinner':
                 'skinner'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='skinner',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
