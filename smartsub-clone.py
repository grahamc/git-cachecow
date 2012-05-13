#!/usr/bin/python

import subprocess, os

was = os.getcwd()

gitsub = subprocess.check_output('smartsub.py')
for line in gitsub.split("\n"):
    if line:
        args = line.split()
        args.insert(0, 'cachehash.sh')
        subprocess.call(args)

        os.chdir(args[2])
        subprocess.call(['smartsub-clone.py'])
        os.chdir(was)

