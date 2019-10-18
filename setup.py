#!/usr/bin/env python3
import re
import setuptools


with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
        name='timesnake',
#        scripts=[],
        version='0.0.1',
        author='Lorenzo Gaifas',
        author_email='brisvag@gmail.com',
        description='',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/DnPy/timesnake',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
            'Operating System :: OS Independent',
        ],
        install_requires=requirements,
        python_requires='>=3.5',
#        package_data={'': []}
        )

