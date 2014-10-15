#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='morgan',
    version='1.0',
    description="",
    author="nGen Works",
    author_email='info@ngenworks.com',
    url='',
    packages=find_packages(),
    package_data={'morgan': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
