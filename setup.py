# -*- coding: utf-8 -*-
"""
This module contains the tool of bodleian.recipe.apache
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.3.2'

long_description = (
    read('README.txt')
    + '\n' +
    read('bodleian', 'recipe', 'apache', 'building.txt')
    + '\n\n' +
    read('bodleian', 'recipe', 'apache', 'configuring.txt')
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '==============\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '========\n'
    )
entry_point = 'bodleian.recipe.apache:Recipe'
entry_points = {"zc.buildout": [
              "build = bodleian.recipe.apache:BuildRecipe",
              "config = bodleian.recipe.apache:ConfigureRecipe",
              #"instance = bodleian.recipe.apache:ConfigureRecipe",
              ]}

tests_require=['zope.testing', 'zc.buildout', 'Cheetah']

setup(name='bodleian.recipe.apache',
      version=version,
      description="An zc buildout for build and configure apache",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='bodleian recipe apache configure',
      author='Paris sprint 2008',
      author_email='products-developers@lists.bodleian.org',
      url='https://github.com/BDLSS/bodleian.recipe.apache.git',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bodleian', 'bodleian.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        # -*- Extra requirements: -*-
                        'zc.recipe.cmmi',
                        "Cheetah>=2.4.4",
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'bodleian.recipe.apache.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
