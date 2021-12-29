#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as file_obj:
    long_description = file_obj.read()

install_requires = [
    "backoff",
    "requests",
    "argparse",
    "singer-python"
]


setup(name='python-outreach',
      version='1.0.0',
      description="Python-outreach is a Python wrapper functions for Outreach APIs",
      author="Pramod Toraskar",
      long_description=long_description,
      url='https://github.com/ptoraskar/python-outreach.git',
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "Operating System :: OS Independent"
      ],
      py_modules=['python_outreach'],
      install_requires=install_requires,
      entry_points='''
          [console_scripts]
          python-outreach=python_outreach:main
      ''',
      packages=['python_outreach'],
      include_package_data=True,
      package_data = {
          'python_outreach': ['schemas/*.json'],
      }
)
