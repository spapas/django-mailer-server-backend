#!/usr/bin/env python

from distutils.core import setup

setup(name='mailer_server_backend',
      version='0.1',
      description='A django mail backend for mailer server',
      author='Serafeim Papastefanos',
      author_email='spapas@gmail.com',
      url='https://github.com/spapas/django-mailer-server-backend',
      packages=['mailer_server_backends'],
     )
