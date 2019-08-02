"""
.. module:: setup
   :synopsis: Installation information for django-version-endpoint
.. moduleauthor:: Propylon
"""
# Standard
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

INSTALL_REQUIRES = ['setuptools', 'Django>=1.11']


setup(
    name='django-version-endpoint',
    version='1.0.4',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='Apache-2.0',
    description='Provide an endpoint to query installed python package '
                'versions',
    long_description=README,
    url='https://github.com/propylon/django-version-endpoint',
    author='Propylon',
    author_email='opensource@propylon.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=INSTALL_REQUIRES,
)
