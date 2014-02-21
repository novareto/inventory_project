from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='inventory',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'dolmen.forms.crud',
          # -*- Extra requirements: -*-
      ],
      entry_points={
         'fanstatic.libraries': [
            'inventory = inventory.resources:library',
         ],
         'paste.app_factory': [
             'app = inventory.utils:app_factory',
         ],
      }
      )
