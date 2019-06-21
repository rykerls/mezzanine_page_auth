# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from setuptools import setup, find_packages

try:
    readme = open('README.rst', encoding='utf-8').read()
except:
    readme = open('README.rst').read()    

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'mezzanine >= 1.4.0',
]

from mezzanine_page_auth import __version__ as version

setup(
    name='mezzanine-page-auth',
    version=version,
    author='Ryker Schwartzenberger',
    author_email='rykerls@protonmail.com',
    description='A Mezzanine module for add group-level permission to pages.',
    long_description=readme,
    license='BSD License',
    url='https://github.com/rykerls/mezzanine_page_auth/',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    test_suite='runtests.runtests',
    tests_require=['mock', 'pep8', 'pyflakes', 'factory_boy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
