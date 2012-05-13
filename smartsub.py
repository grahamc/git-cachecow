#!/usr/bin/python

import subprocess, re, sys
from copy import deepcopy

try:
    gm = open('.gitmodules')
except IOError as e:
    sys.exit(0)

data = {}
d_row = {
        "key": None,
        "uri": None,
        "path": None
}
row = deepcopy(d_row)

sub_name = re.compile('^\[submodule "(.*?)"]$')
sub_path = re.compile('^path = (.*?)$')
sub_uri = re.compile('^url = (.*?)$')
for line in gm:
    line = line.strip()
    m = sub_name.search(line)
    if m:
        row['key'] = m.group(1)

    p = sub_path.search(line)
    if p:
        row['path'] = p.group(1)

    u = sub_uri.search(line)
    if u:
        row['uri'] = u.group(1)
    if row['key'] and row['uri'] and row['path']:
        data[row['key']] = row
        row = deepcopy(d_row)

sub_hash = re.compile('^-(.*?) (.*?)$')
gf = subprocess.check_output('git submodule', shell=True).split("\n")
for line in gf:
    h = sub_hash.search(line)
    if h:
        data[h.group(2)]['cid'] = h.group(1)

for key, row in data.iteritems():
    print "%s\t%s\t%s" % (row['uri'], row['path'], row['cid'])

