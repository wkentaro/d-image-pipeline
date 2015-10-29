#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
from setuptools import setup, find_packages


setup(
    name='drf',
    version='0.1',
    packages=find_packages(),
    description='Deep recognition flow.',
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/drf',
    install_requires=open('requirements.txt').readlines(),
    license='MIT',
    keywords='recognition, machine-learning',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        ],
)
