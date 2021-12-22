#!/usr/bin/env python

from setuptools import setup

setup(name='python-outreach',
      version='0.7.0',
      description='Python-outreach is a Python wrapper functions for Outreach APIs',
      author='Pramod Toraskar',
      url='',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['python_outreach'],
      install_requires=[
          'backoff==1.8.0',
          'requests==2.23.0',
          'singer-python==5.9.0'
      ],
      entry_points='''
          [console_scripts]
          python-outreach=python_outreach:main
      ''',
      packages=['python_outreach'],
      package_data = {
          'python_outreach': ['schemas/*.json'],
      }
)
