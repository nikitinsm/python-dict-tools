#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup\
    ( name='dict_tools'
    , version='1.0'
    , description='Tools for working with big and npredictable data structures'
    , author='Sergey Nikitin'
    , author_email='nikitinsm@gmail.com'
    , url='https://github.com/nikitinsm/python-dict-tools'
    , packages=find_packages('src')
    , package_dir={'': 'src'}
    , include_package_data=True
    )
