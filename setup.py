#!/usr/bin/env python
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='django-mailer-server-backend',
    version='0.3.0',
    description="A django mail backend for mailer server (https://github.com/spapas/mailer_server)",
    long_description=readme(),
    author='Serafeim Papastefanos',
    author_email='spapas@gmail.com',
    license='MIT',
    url='https://github.com/spapas/django-mailer-server-backend',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['tests.*', 'tests',]),

    install_requires=['Django >= 1.11', 'six'],

    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
