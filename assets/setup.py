# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('{{.Title}}/__init__.py', 'r', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='{{.Title}}',
    version=version,
    author='{{.Author}}',
    author_email='{{.Email}}'
    maintainer='{{.Author}}',
    maintainer_email='{{.Email}}',
    description='{{.Description}}',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            '{{.Title}} = {{.Title}}.cli:main'
        ]
    }
)
