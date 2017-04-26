#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.7'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='zappa-file-widget-mediabucket',
    version=version,
    description="""Django Admin File Wiget for Zappa based admin panels, forked to allow use of a different bucket for media files""",
    long_description="This has to be forked, hopefully temporarily, as upstream is not responding (3 months)",
    author='Matías Pizarro',
    author_email='matias@pizarro.net',
    url='https://github.com/rebost/zappa-file-widget',
    packages=[
        'zappa_file_widget',
    ],
    include_package_data=True,
    install_requires=required,
    license="MIT",
    zip_safe=False,
    keywords='zappa-file-widget',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
