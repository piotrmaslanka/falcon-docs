# coding=UTF-8
from setuptools import setup, find_packages

setup(packages=find_packages(include=['falcondocs', 'falcondocs.*']),
      install_requires=["falcon", "six"],
      tests_require=[
          "nose", "mock", "coverage"
      ],
      test_suite='nose.collector'
      )
