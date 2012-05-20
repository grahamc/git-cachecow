#!/usr/bin/python

from distutils.core import setup

setup(name='git-cachecow',
        version='0.1',
        py_modules=[
            'backwards',
            'git-cclone',
            'git-scclone',
            'git-submodule-describe',
            'git-submodule-cclone'
        ])
