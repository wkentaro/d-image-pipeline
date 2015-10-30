#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='dip',
    version='0.1',
    package_dir={'': 'lib'},
    packages=find_packages(),
    description='deep image pipeline',
    long_description=open('README.rst').read(),
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/d-image-pipeline',
    install_requires=open('requirements.txt').readlines(),
    license='MIT',
    keywords='machine-learning',
)
