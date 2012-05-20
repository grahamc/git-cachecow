#!/usr/bin/python

from distutils.core import setup

setup(name='git-cachecow',
        version='0.1',
        url='https://github.com/grahamc/git-cachecow',
        author='Graham Christensen',
        author_email='graham@grahamc.com',
        description='Cache git clone and git submodules in a cache directory.',
        py_modules=[
            'backwards'
        ],
        scripts=[
            'git-cclone',
            'git-scclone',
            'git-submodule-describe',
            'git-submodule-cclone'
        ])
